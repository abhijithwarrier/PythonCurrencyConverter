# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO CONVERT USER-INPUT AMOUNT FROM SELECTED CURRENCY VALUE TO SELECTED CURRENCY
# BASED ON REAL-TIME CURRECNY RATES
#
# GET YOUR FREE API KEY FROM : https://www.alphavantage.co

# Importing necessary packages
import requests
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

# Making a list of currencies. You can add more items (currencies) to the list
currencyList = ['INR', 'USD', 'AED', 'AUD', 'BHD', 'BRL', 'CAD', 'CNY', 'EUR', 'HKD',
                'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'JPY', 'HUF', 'RON', 'MYR', 'SEK',
                'SGD', 'CHF', 'KRW', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RUB', 'MXN',
                'CZK', 'PLN', 'PHP', 'ZAR']

# Defining CreateWidgets() to create necessary widgets for the GUI
def CreateWidgets():
    inputAMT_Label = Label(root, text="AMOUNT : ", bg="peachpuff4")
    inputAMT_Label.grid(row=1, column=0, padx=5, pady=5)
    iAMT = Entry(root, width=14, textvariable=getAMT, bg="snow3", font=('',20), justify="center")
    iAMT.grid(row=1, column=2, padx=5, pady=5)

    fromLabel = Label(root, text="FROM : ", bg="peachpuff4")
    fromLabel.grid(row=2, column=0, padx=5, pady=5)
    root.fromList = Combobox(root, width=10, values=currencyList, state="readonly")
    root.fromList.grid(row=3, column=0, padx=5, pady=5)
    root.fromList.set("INR")

    toLabel = Label(root, text="TO : ", bg="peachpuff4")
    toLabel.grid(row=2, column=2, padx=5, pady=5)
    root.toList = Combobox(root, width=10, values=currencyList, state="readonly")
    root.toList.grid(row=3, column=2, padx=5, pady=5)
    root.toList.set("INR")

    convertButton = Button(root, text="CONVERT", width=15, command=Convert)
    convertButton.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    exrateLabel = Label(root, text="EXCHANGE RATE : ",bg="peachpuff4")
    exrateLabel.grid(row=5, column=0, padx=5, pady=5, columnspan=2)
    root.exrate = Label(root, width=14, font=('',20), bg='snow3',  justify="center")
    root.exrate.grid(row=5, column=2, padx=5, pady=5)

    outputLabel = Label(root, text="CONVERTED AMT : ", bg="peachpuff4")
    outputLabel.grid(row=6, column=0,padx=5, pady=5, columnspan=2)
    root.outputAMT = Label(root, width=14, font=('',20), bg="snow3", justify="center")
    root.outputAMT.grid(row=6, column=2, padx=5, pady=5, columnspan=2)

# Defining Convert() function for converting the curreny
def Convert():
    # Fetching & storing user-inputs in resepective variables
    # Converting user-input amount which is a string into float type
    inputAmt = float(getAMT.get())
    from_Currency = root.fromList.get()
    to_Currency = root.toList.get()

    # Storing the API Key from https://www.alphavantage.co/
    apiKey = "Y2ULPCBPVNI7CD31"
    # Storing the base URL
    baseURL = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    # Storing the complete URL
    reqURL = baseURL+"&from_currency="+from_Currency+"&to_currency="+to_Currency+"&apikey="+apiKey

    # Sending the request to URL & Fetching and Storing the response in response variable
    response = requests.get(reqURL)
    # Returning the JSON object of the response and storing it in result
    result = response.json()
    # Getting the exchange rate (Required Information)
    exchangeRate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
    # Displaying exchange rate in respective label after rounding to 2 decimal places
    root.exrate.config(text=str(round(exchangeRate, 2)))
    # Calculating the converted amount and rounding the decimal to 2 places
    calculateAmt = round(inputAmt * exchangeRate, 2)
    # Displaying the converted amount in the respective label
    root.outputAMT.config(text=str(calculateAmt))

# Creating object of tk class
root = tk.Tk()

# Setting title, background color & size of tkinter window
# & disabling the resizing property
root.geometry("350x250")
root.resizable(False, False)
root.title("PythonCurrenyConverter")
root.config(bg = "peachpuff4")

# Creating tkinter variables
getAMT = StringVar()
fromCurrency = StringVar()
toCurrency = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
