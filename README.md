# PG-Garden

The python based application for Raspberry Pi to control the garden.

## TODO List

- [ ] Prepare this README file.
- [x] Prepare the test instance of the Mqtt Broker on localhost.
- [x] Change the `garden_control.py` file name to `pg-garden.py`. Change also the main folder to `pg-garden`.
- [x] Change `siot` module to `pg` and move all files from the `engine` sub-module to the `pg` module. Remove the `.git` and `.gitignore` files from the `siot` sub-module.
- [x] Change the `config.py` algorithm to use `/etc/opt/` folder to store the default configuration and `$HOME/.config/pg-garden` to read the optional user version of the configuration.
- [x] Cleanup the logging
- [x] Move the application to github.
- [x] Create `pg-garden` shell script that calls the `/opt/pg-garden/pg-garden.py` application.
- [ ] MQTT State and Command topics must be separated (currently it's the same topic). This will allow safe and easy state change reporting and confirmation (currently it's not possible)
- [x] Make the installation script. It should install the application to `/opt/pg-garden`. The script should copy the `pg-garden` shell script to `/usr/local/bin`

## Requirements

### Common

- concurrent.features (`pip3 install futures`)
- paho-mqtt (`pip3 install paho-mqtt`)

### Raspberry Pi (target)

- automationhat (`pip3 install automationhat`)
