import sys
import usocket as socket


CONTENT = b"""\
HTTP/1.0 200 OK

"""

# global client_stream object
client_stream = None


# save the wifi details to a file
def save_file(wifi_name, wifi_pass):
    f = open('wifi.ini', 'w')
    f.write(wifi_name + "\n")
    f.write(wifi_pass)
    f.close()


# serve static web page
def serve_file(filename):
    global client_stream
    client_stream.write(CONTENT)
    with open(filename, 'r') as html:
        client_stream.write(html.read())
    client_stream.close()


# process the web requests
def process_request(req):
    global client_stream
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

            # report back
            serve_file("success.txt")
            return

    # credentials set UI
    serve_file("wifi.txt")


# main loop
def main():
    global client_stream

    s = socket.socket()

    # Binding to all interfaces - server will be accessible to other hosts!
    ap_if = network.WLAN(network.AP_IF)
    sta_if = network.WLAN(network.STA_IF)
    ai = socket.getaddrinfo("0.0.0.0", 80)
    print("Bind address info:", ai)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)

    print("Listening, connect your browser to")
    print(ap_if.ifconfig())
    print(sta_if.ifconfig())

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
        process_request(req)

        print()


# run
main()