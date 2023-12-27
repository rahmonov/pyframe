from pyframe.api import PyFrameAPI
from pyframe.middleware import Middleware

app = PyFrameAPI()

def custom_exception_handler(req, resp, exception_cls):
    resp.text = str(exception_cls)

app.add_exception_handler(custom_exception_handler)

@app.route("/home")
def home(request, response):
    response.text = "Hello from the Home Page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the About Page"

@app.route("/greeting/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"


@app.route("/sum/{num1:d}/{num2:d}")
def sum(request, response, num1, num2):
    total = int(num1) + int(num2)
    response.text = f"{num1} + {num2} = {total}"


@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Books GET Page"
    
    def post(self, req, resp):
        resp.text = "Endpoint to create a book"


def sample_handler(req, resp):
    resp.text = "sample"


app.add_route("/sample", handler=sample_handler)


@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template(
        "index.html", context={"name": "Kiki", "title": "Best Framework"}
    )


@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AssertionError("This error should not be used.")


class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)
    
    def process_response(self, req, resp):
        print("Processing response", req.url)


app.add_middleware(SimpleCustomMiddleware)
