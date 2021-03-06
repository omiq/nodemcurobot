import os
import time
import network


# connect to router
def do_connect(wifi_name, wifi_password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network ' + wifi_name)
        sta_if.active(True)
        sta_if.connect(wifi_name, wifi_password)
        while not sta_if.isconnected():
            print(".", end="")
            time.sleep(0.1)

    print('network config:', sta_if.ifconfig())


# We only want the Access Point if we need to connect
ap = network.WLAN(network.AP_IF)
ap.active(False)

# try to use stored credentials
try:
    # credentials file:
    f = open("wifi.ini", "r")

    # get the wifi name and password from stored file
    contents = f.read()
    wifi_name, wifi_password = contents.split("\n")
    f.close()

    # connect using the acquired deets
    do_connect(wifi_name, wifi_password)

    # Run the robot UI
    exec(open("robot.py").read())

# does the wifi settings file not exist?
except:
    print("File does not exist")
    print("Setting up Access Point")

    # Set up the Access Point
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='ESP8266')
    ap.config(authmode=3, password='0123456789')

    # Start the web server
    exec(open("http_server.py").read())




