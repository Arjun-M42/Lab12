import yfinance as yf

STOCK_DATA = {
    "japan": {
        "exchange": "Tokyo Stock Exchange",
        "indices": {
            "Nikkei 225": "^N225"
        },
        "maps": "https://maps.google.com/?q=Tokyo+Stock+Exchange"
    },
    "india": {
        "exchange": "Bombay Stock Exchange",
        "indices": {
            "Sensex": "^BSESN",
            "Nifty 50": "^NSEI"
        },
        "maps": "https://maps.google.com/?q=Bombay+Stock+Exchange"
    },
    "us": {
        "exchange": "New York Stock Exchange",
        "indices": {
            "S&P 500": "^GSPC",
            "Dow Jones": "^DJI"
        },
        "maps": "https://maps.google.com/?q=New+York+Stock+Exchange"
    }
}

def get_stock_indices(country: str):
    country = country.lower()
    info = STOCK_DATA[country]

    index_values = {}
    for name, symbol in info["indices"].items():
        ticker = yf.Ticker(symbol)
        index_values[name] = ticker.info.get("regularMarketPrice")

    return {
        "exchange": info["exchange"],
        "indices": index_values,
        "map_link": info["maps"]
    }
