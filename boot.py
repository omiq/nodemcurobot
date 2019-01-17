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
            print(".", end = "")
            time.sleep(0.1)
    print('network config:', sta_if.ifconfig())


# try to use stored credentials
try:
    f = open("wifi.ini", "r")

    # get the wifi name and password from stored file
    contents = f.read()
    wifi_name, wifi_password = contents.split("\n")
    f.close()

    # connect using the acquired deets
    do_connect(wifi_name, wifi_password)


# does the wifi settings file not exist?
except:
    print("File does not exist")
    exec (open("http_server.py").read())



