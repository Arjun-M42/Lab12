import requests

MCP_SERVER = "http://localhost:3333"

def plan_trip(city, days, month, interests):
    # Call MCP tool
    weather = requests.get(
        f"{MCP_SERVER}/tools/weather",
        params={"city": city}
    ).json()

    return f"""
### 📍 Cultural & Historical Significance
Tokyo blends ancient traditions like temples and shrines with modern innovation, making it one of the most culturally rich cities in the world.

### 🌤 Weather
- Temperature: {weather['temp']} °C
- Condition: {weather['condition']}

### 🗓 {days}-Day Trip Plan ({month})
**Day 1:** Temples, historic districts  
**Day 2:** Culture, food, shopping  
**Day 3:** Modern Tokyo & landmarks  

### ✈ Flights (Placeholder)
Bangalore → Tokyo | ₹55,000 (approx)

### 🏨 Hotels (Placeholder)
Mid-range hotel near Shinjuku
"""
