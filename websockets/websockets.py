from ws_connection import ClientClosedError

from ws_server import WebSocketServer, WebSocketClient


class TestClient(WebSocketClient):

    def __init__(self, conn):

        super().__init__(conn)
        self.counter = 0

    def process(self):

        try:

            msg = self.connection.read()

            if not msg:
                return

            msg = msg.decode("utf-8")

            items = msg.split(" ")

            cmd = items[0]

            if cmd != "":
                self.counter += 1

                self.connection.write(cmd + str(self.counter))

                print("Responded")

        except ClientClosedError:

            self.connection.close()


class TestServer(WebSocketServer):

    def __init__(self):
        super().__init__("sockets.txt", 2)

    def _make_client(self, conn):
        return TestClient(conn)


server = TestServer()

server.start()

try:

    while True:
        server.process_all()

except KeyboardInterrupt:

    pass

server.stop()


