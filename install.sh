#!/usr/bin/bash

rm -r /opt/pg-garden
mkdir /opt/pg-garden
cp -r mocks /opt/pg-garden
cp -r modules /opt/pg-garden
cp -r pg_iot /opt/pg-garden
cp pg_garden.py /opt/pg-garden
cp LICENSE /opt/pg-garden

rm -r /etc/opt/pg-garden
mkdir /etc/opt/pg-garden
cp config.json /etc/opt/pg-garden

rm /usr/local/bin/pg-garden
cp pg-garden /usr/local/bin

echo pg-garden installed
echo remember to update the configuration file in /etc/opt/pg-garden/config.json