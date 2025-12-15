#!/bin/bash

rm -fR pack/pyharp/*
mkdir -p pack/pyharp/
rm -fR src/pyharp/__pycache__
cp -Rf src/pyharp pack/pyharp/
cp -f etc/install.sh pack/pyharp/
cp -f etc/pyharp.sh pack/pyharp/
chmod +x pack/pyharp/install.sh
chmod +x pack/pyharp/pyharp.sh
