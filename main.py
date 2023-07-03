import requests

URL = "https://api.currencyapi.com/v3/latest?apikey=1zw9ju4YtKzzVva8ch1l3S0fOEcwsBgtu82VueuF"

def convert_currency():
    target_currency = input("Enter the currency code to convert from (e.g., USD): ")
    currency = input("Enter the currency code to convert to (e.g., EUR): ")
    value = 'value'
    parameters = {"code": currency}
    r = requests.get(url=URL, params=parameters)
    data = r.json()

    usd_conversion_rate = 1
    currency_value = data["data"][currency][value]
    target_currency_value = data["data"][target_currency][value]

    amount = float(input("Enter the amount to convert: "))
    converted_amount = amount / target_currency_value
    convert_amount = converted_amount * currency_value

    print(f"{amount} {target_currency} is equal to {convert_amount} {currency}")

convert_currency()
