import requests

MCP = "http://127.0.0.1:3333"

def finance_agent(country: str):
    currency = requests.get(
        f"{MCP}/tools/currency", params={"country": country}
    ).json()

    stocks = requests.get(
        f"{MCP}/tools/stocks", params={"country": country}
    ).json()

    return f"""
### 💱 Official Currency
- **{currency['currency_name']} ({currency['currency_code']})**

### 🔄 Exchange Rates (1 {currency['currency_code']})
- USD: {currency['rates']['USD']}
- INR: {currency['rates']['INR']}
- GBP: {currency['rates']['GBP']}
- EUR: {currency['rates']['EUR']}

### 📈 Major Stock Exchange
- **{stocks['exchange']}**

### 📊 Indices
{chr(10).join([f"- {k}: {v}" for k,v in stocks['indices'].items()])}

### 📍 Stock Exchange HQ
[View on Google Maps]({stocks['map_link']})
"""
