import os
import requests

MCP = os.getenv("MCP_SERVER_URL", "http://127.0.0.1:3333")

def plan_trip(city, days, month, interests):
    weather = None

    try:
        r = requests.get(
            f"{MCP}/tools/weather",
            params={"city": city},
            timeout=5
        )
        if r.status_code == 200:
            weather = r.json()
    except Exception:
        weather = None

    if weather is None:
        weather = {
            "temp": "N/A",
            "condition": "Unavailable (MCP not reachable)"
        }

    return f"""
### 📍 Cultural & Historical Significance
{city} is a globally significant city known for its rich cultural heritage and modern development.

### 🌤 Weather
- Temperature: {weather['temp']}
- Condition: {weather['condition']}

### 🗓 {days}-Day Trip Plan ({month})
Day 1: Historic landmarks  
Day 2: Culture, food & markets  
Day 3: Modern attractions  

✈ Flights and 🏨 hotels are placeholders.
"""
