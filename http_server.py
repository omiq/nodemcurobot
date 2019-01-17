import usocket as socket


CONTENT = b"""\
HTTP/1.0 200 OK

"""


def main():
    s = socket.socket()

    # Binding to all interfaces - server will be accessible to other hosts!
    ai = socket.getaddrinfo("0.0.0.0", 80)
    print("Bind address info:", ai)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening")

    while True:
        res = s.accept()
        client_sock = res[0]
        client_addr = res[1]
        print("Client address:", client_addr)
        print("Client socket:", client_sock)

        # MicroPython socket object
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