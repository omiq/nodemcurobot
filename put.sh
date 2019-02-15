#!/bin/sh

# scripts
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put boot.py
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put main.py
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put blink.py
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put http_server.py
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put wifi.txt
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put success.txt
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put http_server.py

# directory
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put websockets




