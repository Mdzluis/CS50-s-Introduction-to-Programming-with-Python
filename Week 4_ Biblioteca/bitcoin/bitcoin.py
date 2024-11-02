import sys
import requests
import json

# BITCOIN APPLICATION
try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        monto = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# GET BITCOIN RATE INFORMATION IN JSON
respu = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r = respu.json()

# LOCATE THE BITCOIN RATE IN USD IN NESTED DICTIONARIES
for x,y in r["bpi"].items():
    if x == "USD":
        for n,m in y.items():
            if n == "rate_float":
                tasa = m

# USD TO BITCOIN CONVERSION
conversion = monto*tasa
print(f"${conversion:,.4f}")
