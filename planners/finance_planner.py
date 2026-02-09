import os
import requests

MCP = os.getenv("MCP_SERVER_URL", "http://127.0.0.1:3333")

def finance_agent(country):
    currency = None
    stocks = None

    try:
        currency = requests.get(
            f"{MCP}/tools/currency",
            params={"country": country},
            timeout=5
        ).json()
    except Exception:
        pass

    try:
        stocks = requests.get(
            f"{MCP}/tools/stocks",
            params={"country": country},
            timeout=5
        ).json()
    except Exception:
        pass

    if not currency or not stocks:
        return "⚠ Live MCP tools unavailable in cloud deployment."

    return f"""
### 💱 Official Currency
{currency['currency_name']} ({currency['currency_code']})

### 🔄 Exchange Rates (1 {currency['currency_code']})
USD: {currency['rates']['USD']}  
INR: {currency['rates']['INR']}  
GBP: {currency['rates']['GBP']}  
EUR: {currency['rates']['EUR']}  

### 📈 Stock Exchange
{stocks['exchange']}

### 📊 Indices
{chr(10).join([f"- {k}: {v}" for k,v in stocks['indices'].items()])}

### 📍 Location
[View on Google Maps]({stocks['map_link']})
"""
