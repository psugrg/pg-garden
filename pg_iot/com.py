import logging
import time
from paho.mqtt import client
from pg_iot import config


def publish(params):
    event, modules, session = params

    logging.info("START Communication")
    while not event.is_set():
        for module in modules:
            for pub in module.pubs:
                while not pub.queue.empty():
                    message = pub.queue.get(False)
                    logging.info("Publishing: " + pub.topic + " " + message)
                    session.publish(pub.topic, message, 0, False)
        time.sleep(0.1)

    logging.info("STOP Communication")


def on_message(session, userdata, msg):
    logging.debug("[" + msg.topic + "]" + " "+str(msg.payload))
    for module in userdata:
        for sub in module.subs:
            if msg.topic == sub.topic:
                sub.queue.put(msg.payload)


def on_connect(session, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server """

    logging.info("Connection to MQTT Broker established")
    logging.debug("Result code: "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for module in userdata:
        for sub in module.subs:
            session.subscribe(sub.topic)
            logging.debug("Subscribed to: " + sub.topic)


def connect(conf: config.Config, modules):
    """ Connect to the MQTT Broker """

    # Read configuration
    configuration = conf.get("broker")

    # Setup the client connection
    session = client.Client(userdata=modules)
    session.on_connect = on_connect
    session.on_message = on_message
    if True == configuration["tls"]:
        session.tls_set()
    if False == configuration["anonymus"]:
        password = configuration["passwd"]
        session.username_pw_set(configuration["username"], password)

    session.connect(configuration["addr"], configuration["port"], 60)

    # Start the network loop threaded interface
    session.loop_start()

    return session
