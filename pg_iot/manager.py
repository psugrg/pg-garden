import concurrent.futures
import threading
import queue
from pg_iot import com
from pg_iot import config


def start(conf: config.Config, modules):

    # Create queues for feeds
    for module in modules:
        for sub in module.subs:
            sub.queue = queue.Queue(maxsize=10)
        for pub in module.pubs:
            pub.queue = queue.Queue(maxsize=10)

    # Connect to the external broker
    client = com.connect(conf, modules)

    # Create an event for sending exit signal to threads
    event = threading.Event()

    # Start Actors threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(com.publish, list((event, modules, client)))
        for module in modules:
            executor.submit(module.run, event)

    # Disconnect from the external broker
    client.disconnect()
