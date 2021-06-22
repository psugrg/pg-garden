import logging
from pg_iot import manager
from pg_iot import config
from modules import gardena_wda
from modules import controller
from modules import temp_hum

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("pg_iot Garden Controller application start")

    conf = config.Config("pg-garden")

    manager.start(conf, [
        gardena_wda.Watering(conf, "sprinklers_program_1"),
        gardena_wda.Watering(conf, "sprinklers_program_2"),
        gardena_wda.Watering(conf, "sprinklers_program_3"),
        temp_hum.Temp_hum(conf),
        controller.Controller()
    ])
