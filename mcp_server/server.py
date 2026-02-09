from fastapi import FastAPI
from tools.weather_tool import get_weather
from tools.currency_tool import get_currency_rates
from tools.stock_tool import get_stock_indices

app = FastAPI(title="GenAI MCP Server")

@app.get("/health")
def health():
    return {"status": "ok"}

# ---------- Problem 1 ----------
@app.get("/tools/weather")
def weather(city: str):
    return get_weather(city)

# ---------- Problem 2 ----------
@app.get("/tools/currency")
def currency(country: str):
    return get_currency_rates(country)

@app.get("/tools/stocks")
def stocks(country: str):
    return get_stock_indices(country)
