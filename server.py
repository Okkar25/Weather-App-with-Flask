from flask import Flask, render_template, request, redirect, url_for
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    # return "Hello World"
    return render_template("index.html")


@app.route("/weather", methods=["POST", "GET"])
def get_weather():
    if request.method == "POST":
        city = request.form["city"]
    elif request.method == "GET":
        # Handle GET request if needed (e.g., if someone tries to access the URL directly)
        city = request.args.get("city")

    # if city is empty
    if not city:
        return redirect(url_for("index"))
    # if city name is starting with white spaces
    elif not bool(city.strip()):
        city = "Utah"

    weather_data = get_current_weather(city)

    if weather_data:
        return render_template(
            "weather.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].title(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}",
            weather_icon=weather_data["weather"][0]["icon"],
        )
    else:
        # if city name is not found or invalid city name => redirect to error page
        error_message = f"Could not retrieve weather for '{city}'. Please check the city name and try again."
        return render_template("error.html", error_message=error_message)


@app.route("/about")
def about():
    return "This is About Page"


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    serve(app, host="0.0.0.0", port=8000)
