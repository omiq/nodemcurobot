#!/bin/sh

# scripts
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put boot.py
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put main.py
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put blink.py
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put http_server.py
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put wifi.txt
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put success.txt
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put http_server.py
echo .

# robot control
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put websockets.py
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put sockets.html
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put ws_connection.py
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put ws_server.py
echo .
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART put motest.py





