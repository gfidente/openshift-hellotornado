import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

def main(address):
    application.listen(8080, address)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    address = "127.0.0.1"
    main(address)
