import csv
import time
import requests

API_URL = "https://www.bitstamp.net/api/v2/ticker/btcusd/"

with open("btcusdPrice.csv", "a", newline="") as outfile:
    writer = csv.writer(outfile)
    try:
        while True:
            response = requests.get(API_URL, timeout=10)
            response.raise_for_status()
            price = response.json()["last"]
            print(price)
            writer.writerow([price])
            outfile.flush()
            time.sleep(3)
    except KeyboardInterrupt:
        pass

