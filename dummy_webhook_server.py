#!python3
"""
Written by M. Shalahuddin Yahya S. (yahya@qlue.id)
"""
from tornado import httpserver, ioloop, web


class RESTAPI:
    def __init__(self):
        self.name = "REST API"
        self.io_loop = None
        self.http_server = None

    def run(self):
        self.io_loop = ioloop.IOLoop()
        application = web.Application([
            (r"/", DummyHandler),
            (r"/api/testing", DummyHandler)
        ])
        self.http_server = httpserver.HTTPServer(application)
        self.http_server.listen(5000)
        print("Start")
        self.io_loop.start()

    def stop(self):
        self.http_server.stop()
        self.io_loop.stop()


class BaseHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers",
                        "x-requested-with,access-control-allow-origin,authorization,content-type")
        self.set_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")

    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class NullHandler(BaseHandler):
    async def get(self):
        self.set_status(200)

    async def post(self):
        self.set_status(200)


class DummyHandler(BaseHandler):
    async def get(self):
        print("GET success!")
        self.write("Success!")
        self.set_status(200)

    async def post(self):
        headers = self.request.headers
        print(headers)
        body = self.request.body
        if len(body) > 500:
            print(body[:500])
            print(".\n.\n.")
            print(body[-500:])
        else:
            print(body)
        print("\n\n\n\n\n")


class DumpHandler(BaseHandler):
    async def get(self):
        self.write("Success!")
        self.set_status(200)

    async def post(self):
        headers = self.request.headers
        print(headers)
        with open("dump.bin", "wb") as _fp:
            _fp.write(self.request.body)
        print("Successfully dumped!")


def main():
    rest_api = RESTAPI()
    try:
        rest_api.run()
    except KeyboardInterrupt:
        rest_api.stop()


if __name__ == "__main__":
    main()
