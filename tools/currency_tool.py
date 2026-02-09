import requests

COUNTRY_CURRENCY = {
    "japan": ("JPY", "Japanese Yen"),
    "india": ("INR", "Indian Rupee"),
    "us": ("USD", "US Dollar"),
    "uk": ("GBP", "British Pound"),
    "south korea": ("KRW", "South Korean Won"),
    "china": ("CNY", "Chinese Yuan")
}

def get_currency_rates(country: str):
    country = country.lower()
    code, name = COUNTRY_CURRENCY.get(country, ("JPY", "Japanese Yen"))

    url = f"https://api.exchangerate-api.com/v4/latest/{code}"
    data = requests.get(url, timeout=5).json()

    return {
        "currency_name": name,
        "currency_code": code,
        "rates": {
            "USD": data["rates"].get("USD"),
            "INR": data["rates"].get("INR"),
            "GBP": data["rates"].get("GBP"),
            "EUR": data["rates"].get("EUR"),
        }
    }
