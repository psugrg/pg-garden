import logging
from pg_iot import actor


class Controller(actor.Actor):
    def run(self, event):
        logging.info("START Controller")
        input("Press Enter to quit!\n")
        event.set()
        print("Closing application...")
        logging.info("STOP Controller")
