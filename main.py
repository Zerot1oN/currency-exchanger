import requests
import tkinter as tk

URL = "https://api.currencyapi.com/v3/latest?apikey=1zw9ju4YtKzzVva8ch1l3S0fOEcwsBgtu82VueuF"

def convert_currency():
    target_currency = target_entry.get()
    currency = currency_entry.get()

    parameters = {"code": currency}
    r = requests.get(url=URL, params=parameters)
    data = r.json()

    usd_conversion_rate = 1
    currency_value = data["data"][currency]['value']
    target_currency_value = data["data"][target_currency]['value']

    amount = float(amount_entry.get())
    converted_amount = amount / target_currency_value
    convert_amount = converted_amount * currency_value

    result_label.config(text=f"{amount} {target_currency} is equal to {convert_amount} {currency}")

window = tk.Tk()
window.title("Currency Converter")
amount_label = tk.Label(window, text="Amount to Convert:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()
target_label = tk.Label(window, text="Target Currency (e.g. EUR):")
target_label.pack()
target_entry = tk.Entry(window)
target_entry.pack()
currency_label = tk.Label(window, text="Currency to Convert (e.g. USD):")
currency_label.pack()
currency_entry = tk.Entry(window)
currency_entry.pack()
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()
