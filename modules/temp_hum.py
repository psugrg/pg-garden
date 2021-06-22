import logging
import time
from pg_iot import actor
from pg_iot import config
try:
    import Adafruit_DHT
except ImportError:
    import mocks.Adafruit_DHT as Adafruit_DHT


class Temp_hum(actor.Actor):
    def __init__(self, conf: config.Config):
        # This Actor has it's own constructor that overrides parent constructor

        configuration = conf.get("temperature_and_humidity")

        # Call parent constructor with the topics (the same for subscribe and publish)
        super().__init__(configuration["mqtt"])

    def run(self, event):
        logging.info("START Temperature & Humidity Sensor")

        while not event.is_set():
            # Read temperature and humidity values from ext. sensor
            logging.debug("read DHT")
            humidity, temperature = Adafruit_DHT.read_retry(22, 4)
            logging.debug("read done!")
            # Verify readings
            if humidity is not None and temperature is not None:
                logging.debug("Result: T:" + str(temperature) +
                              " H:" + str(humidity))
                super().put_message("temperature",
                                    "{0:0.1f}".format(temperature))
                super().put_message("humidity", "{0:0.1f}".format(humidity))
            else:
                logging.debug("DHT reading failed")
            time.sleep(10)
        logging.info("STOP Temperature & Humidity Sensor")
