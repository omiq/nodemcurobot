# exec(open("http_server.py").read())

import machine
import usocket as socket
import network


CONTENT = b"""\
HTTP/1.0 200 OK
"""

# save the wifi details to a file
def save_file(wifi_name, wifi_pass):
    f = open('wifi.ini', 'w')
    f.write(wifi_name + "\n")
    f.write(wifi_pass)
    f.close()

# main loop that listens for connections
def main():
    ap_if = network.WLAN(network.AP_IF)
    sta_if = network.WLAN(network.STA_IF)
    s = socket.socket()

    # Binding to all interfaces - server will be accessible to other hosts!
    ai = socket.getaddrinfo("0.0.0.0", 80)
    print("Bind address info:", ai)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to")
    print(ap_if.ifconfig())

    while True:
        res = s.accept()
        client_sock = res[0]
        client_addr = res[1]
        print("Client address:", client_addr)
        print("Client socket:", client_sock)

        client_stream = client_sock

        print("Request:")
        req = client_stream.readline()
        print(req)


        while True:
            h = client_stream.readline()
            if h == b"" or h == b"\r\n":
                break
            print(h)

        client_stream.write(CONTENT)
        with open('wifi.txt', 'r') as html:
            client_stream.write(html.read())

        client_stream.close()
        print()


main()