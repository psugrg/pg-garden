#!/bin/sh

# Install application files
rm -r /opt/pg-garden
mkdir /opt/pg-garden
cp -r mocks /opt/pg-garden
cp -r modules /opt/pg-garden
cp -r pg_iot /opt/pg-garden
cp pg_garden.py /opt/pg-garden
cp LICENSE /opt/pg-garden

# Install configuration files
mkdir -p /etc/opt/pg-garden
cp config.json /etc/opt/pg-garden

# Install launcher
rm /usr/local/bin/pg-garden
cp pg-garden /usr/local/bin

# Enable PG Garden systemd service
systemctl disable pg-garden.service
mv pg-garden.service /lib/systemd/system
systemctl daemon-reload
systemctl enable pg-garden.service

echo pg-garden installed
echo remember to update the configuration file in /etc/opt/pg-garden/config.json