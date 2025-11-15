import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = "YOUR_API_KEY_HERE"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Could not retrieve bitcoin price")


    data = response.json()
    try:
        price_usd_str = data["data"]["priceUsd"]
        price_usd = float(price_usd_str)
    except (KeyError, TypeError, ValueError):
        sys.exit("Unexpected API response format")

    cost = price_usd * n
    print(f"${cost:,.4f}")

if __name__ == "__main__":
    main()

