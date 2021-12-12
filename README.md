# Garden controller application

Python based application running on the Rasspberry Pi.

This application is primarily a playground to practice python based automation.

The application suses MQTT protocol for communication and cane easily be paired
with any home automation system that supports it (like i.e. Home Assistant.)

The main porpoise of this application (as for today) is to act as the controller
for the sprinkler system based on the Gardena Water Disrtiputor Automatic.

![pg-garden diagram](/pg-garden-diagram.jpg)

## TODO List

- [x] Prepare this README file.
- [x] Prepare the test instance of the Mqtt Broker on localhost.
- [x] Change the `garden_control.py` file name to `pg-garden.py`.
 Change also the main folder to `pg-garden`.
- [x] Change `siot` module to `pg` and move all files from the `engine`
 sub-module to the `pg` module. Remove the `.git` and `.gitignore` files from the
 `siot` sub-module.
- [x] Change the `config.py` algorithm to use `/etc/opt/` folder to store the
 default configuration and `$HOME/.config/pg-garden` to read the optional user
 version of the configuration.
- [x] Cleanup the logging
- [x] Move the application to github.
- [x] Create `pg-garden` shell script that calls the
 `/opt/pg-garden/pg-garden.py` application.
- [ ] MQTT State and Command topics must be separated (currently it's the same
 topic). This will allow safe and easy state change reporting and confirmation
 (currently it's not possible)
- [x] Make the installation script. It should install the application to
 `/opt/pg-garden`. The script should copy the `pg-garden` shell script to
 `/usr/local/bin`
- [x] Make `pg-garden` `systemd` service to automatically start the application
 on startup

## Requirements

### Common

- concurrent.features (`pip3 install futures`)
- paho-mqtt (`pip3 install paho-mqtt`)

### Raspberry Pi (target)

- automationhat (`pip3 install automationhat`)

## Useful Development Information

### Debugging

use `journalctl -r` command to analyze logs from the `systemd`
(errors from python will be present)
