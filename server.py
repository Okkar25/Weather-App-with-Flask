from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    # return "Hello World"
    return render_template("index.html")


@app.route("/about")
def about():
    return "This is About Page"


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    serve(app, host="0.0.0.0", port=8000)
