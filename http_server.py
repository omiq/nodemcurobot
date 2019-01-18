import sys
import usocket as socket


CONTENT = b"""\
HTTP/1.0 200 OK

"""


# save the wifi details to a file
def save_file(wifi_name, wifi_pass):
    f = open('wifi.ini', 'w')
    f.write(wifi_name + "\n")
    f.write(wifi_pass)
    f.close()


# process the web requests
def process_request(client_stream, req):

    # defaults
    method = ""
    url = ""
    wifi_pass = ""
    wifi_name = ""

    # is it an actual request?
    if (str(req).find(" ") > 1):
        request_attributes = req.split(b" ")
        method = request_attributes[0]
        url = str(request_attributes[1])

        # is there a query?
        if (str(url).find("?") > 1):
            query_slug, query_params = url.split("?")
            query_params = query_params.split("&")

            for query_var in query_params:
                var_name, var_val = query_var.split("=")
                print("{} -> {}".format(var_name, var_val))
                if (var_name == "name"): wifi_name = var_val.replace("+", " ")
                if (var_name == "pass"): wifi_pass = var_val.replace("+", " ")

            print("{}\n{}\n\n".format(method, url))
            print("Name:{}\nPassword:{}\n\n".format(wifi_name, wifi_pass))

            # write the deets away
            save_file(wifi_name, wifi_pass)

            # quit
            sys.exit()


    client_stream.write(CONTENT)
    with open('wifi.txt', 'r') as html:
        client_stream.write(html.read())


# main loop
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

        # deal with the request
        process_request(client_stream, req)

        client_stream.close()
        print()


main()