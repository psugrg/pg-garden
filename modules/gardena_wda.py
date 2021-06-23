# Controlls the Gardena Water Distributor Automatic
# It's supposed to be used together with one water valve that will be controlled by this actor

import logging
import time
import threading
from pg_iot import config
from pg_iot import actor
try:
    import automationhat
except ImportError:
    import mocks.automationhat as automationhat

lock = threading.Lock()


class Watering(actor.Actor):
    def __init__(self, conf: config.Config, program: str):
        # This Actor has it's own constructor that overrides parent constructor

        configuration = conf.get(program)

        sequence_config = configuration["sequence_config"]
        mqtt_water_valve = configuration["mqtt"]["subscribe&publish"]["water_valve"]
        self.program_name = configuration["name"]

        # Internal fields needed by the Watering actor
        self.break_active = False
        self.topic = "water_valve"
        self.topic_status = "status"
        self.message_on = mqtt_water_valve["payloads"]["open"]
        self.message_off = mqtt_water_valve["payloads"]["close"]
        self.switching_time = sequence_config["switching_time"]
        self.off_time = sequence_config["off_time"]
        self.sequence = sequence_config["sequence"]

        # Call parent constructor with the topics (the same for subscribe and publish)
        super().__init__(configuration["mqtt"])

    def sleep_break(self, delay):
        for t in range(delay):
            logging.debug("sleep: " + str(t))
            time.sleep(1)
            if bytes(self.message_off, "utf8") == super().get_message(self.topic):
                logging.info(
                    "INTERRUPT: Request Stop [" + self.program_name + "]")
                self.break_active = True
            if True == self.break_active and t >= self.switching_time - 1:
                break

    def run_sequence(self):
        logging.info("Water sequence start [" + self.program_name + "]")
        self.break_active = False
        # super().put_message(self.topic, self.message_on)

        for op_name, duration in self.sequence:
            logging.debug("Operation: " + op_name +
                          ", duration: " + str(duration))
            super().put_message(self.topic_status, op_name)

            logging.debug("Valve activate")
            automationhat.relay.one.on()
            self.sleep_break(duration)

            logging.debug("Valve deactivate")
            automationhat.relay.one.off()
            self.sleep_break(self.off_time)

        logging.info("Water sequence stop [" + self.program_name + "]")
        super().put_message(self.topic, self.message_off)
        super().put_message(self.topic_status, "Idle")
        automationhat.relay.one.off()

    def run(self, event):
        logging.info(
            "START Gardena Water Distributor Automatic [" + self.program_name + "]")
        super().put_message(self.topic_status, "Idle")

        for op_name, duration in self.sequence:
            logging.debug("Operation: " + op_name +
                          ", duration: " + str(duration))

        while not event.is_set():
            message = super().get_message(self.topic)

            if bytes(self.message_on, "utf8") == message:
                with lock:
                    self.run_sequence()

            time.sleep(0.1)

        logging.info(
            "STOP Gardena Water Distributor Automatic [" + self.program_name + "]")
