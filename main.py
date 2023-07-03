import requests
from tkinter import *
from tkinter import ttk

URL = "https://api.currencyapi.com/v3/latest?apikey=1zw9ju4YtKzzVva8ch1l3S0fOEcwsBgtu82VueuF"


def info():
    infow = Tk()
    infow.title("Currency Helper")
    infow.geometry("245x300")
    infow.attributes("-toolwindow", True)
    text = Label(infow,text="Hello, this is currency helper. \n It helps you find currencies. \n These are the most popular ones")
    text.pack()
    clist = Label(infow,text="US Dollar - USD \n Euro - EUR \n Japanese Yen - JPY \n British Pound - GBP \n Swiss Franc - CHF \n Canadian Dollar - CAD \n Australian Dollar - AUD \n New Zealand Dollar - NZD \n Chinese Yuan - CNY \n Indian Rupee - INR \n Mexican Peso - MXN \n Brazilian Real - BRL \n South Korean Won - KRW \n Russian Rouble - RUB")
    clist.pack()

def convert_currency():
    target_currency = target_entry.get()
    currency = currency_entry.get()

    parameters = {"code": currency}
    r = requests.get(url=URL, params=parameters)
    data = r.json()

    usd_conversion_rate = 1
    currency_value = data["data"][currency]['value']
    target_currency_value = data["data"][target_currency]['value']
    date = data["meta"]["last_updated_at"]

    amount = float(amount_entry.get())
    converted_amount = amount / target_currency_value
    convert_amount = converted_amount * currency_value

    result_label.config(text=f"{amount} {target_currency} is equal to {convert_amount} {currency} (Last updated at {date})")

window = Tk()
window.title("Currency Converter")
window.geometry("500x250")
window.minsize(200,150)
icon = PhotoImage(file = "icon1.png")
window.iconphoto(False, icon)
window.attributes("-toolwindow", True)

amount_label = Label(window, text="Amount to Convert:")
amount_label.pack()

amount_entry = Entry(window)
amount_entry.pack()

target_label = Label(window, text="Target Currency (e.g. EUR):")
target_label.pack()

target_entry = Entry(window)
target_entry.pack()

currency_label = Label(window, text="Currency to Convert (e.g. USD):")
currency_label.pack()

currency_entry = Entry(window)
currency_entry.pack()

convert_button = ttk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

btn1 = ttk.Button(text="Currency Helper", command=info)
btn1.pack()


result_label = Label(window, text="")
result_label.pack()

window.mainloop()
