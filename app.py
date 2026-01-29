from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = "21b9868409ab5e3cd9181caa267819f3"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city,
                "temp": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"].title(),
                "wind": data["wind"]["speed"]
            }
        else:
            error = "City not found or API error"

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
