from typing import List
import json
import sys
import pathlib
import logging


class Config:
    def __init__(self, app_name: str) -> None:
        self.config_folder_name = app_name

    def get(self, module: str) -> List[str]:
        """Returns the list containing a configuration for a give module"""

        try:
            with open(pathlib.Path().home().__str__() + "/.config/" + self.config_folder_name + "/config.json", "r") as read_file:
                configuration = json.load(read_file)
        except FileNotFoundError:
            try:
                with open("/etc/opt/" + self.config_folder_name + "/config.json", "r") as read_file:
                    configuration = json.load(read_file)
            except FileNotFoundError:
                logging.fatal(
                    "Configuration file missing. Installation broken!")
                sys.exit()

        return configuration[module]
