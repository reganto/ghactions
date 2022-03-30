from tornado.web import Application, url
from tornado.ioloop import IOLoop
from usernado import Handler


class Home(Handler.Web):
    def get(self):
        self.write("Hello")


if __name__ == "__main__":
    Application([url("/", Home, name="home")], debug=True).listen(8000)
    IOLoop.current().start()

