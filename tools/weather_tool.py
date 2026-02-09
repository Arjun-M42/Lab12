import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
print("DEBUG API KEY:", API_KEY)


def get_weather(city):
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        r = requests.get(url, params=params, timeout=5)
        data = r.json()

        return {
            "city": city,
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
    except Exception:
        # fallback (exam-safe)
        return {
            "city": city,
            "temp": "N/A",
            "condition": "Unavailable (fallback mode)"
        }
print("OPENWEATHER_API_KEY =", API_KEY)
