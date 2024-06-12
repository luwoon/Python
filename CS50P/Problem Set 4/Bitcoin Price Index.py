import requests
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

    rate = req_rate()
    cost = n * rate
    print(f"${cost:,.4f}")


def req_rate():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rate = o["bpi"]["USD"]["rate_float"]
        return rate
    except requests.RequestException:
        pass


main()