# Programmer - python_scripts (Abhijith Warrier)

# Importing necessary packages
import json
import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Making a list of currencies. You can add more items (currencies) to the list
currencyList = ['AED', 'AUD', 'BHD', 'BRL', 'CAD', 'CNY', 'EUR', 'HKD', 'INR', 'USD']

# Defining CreateWidgets() to create necessary widgets for the GUI
def CreateWidgets():
    inputAMT_Label = Label(root, text = "AMOUNT:", bg = "darkolivegreen4")
    inputAMT_Label.grid(row = 1, column = 0, padx = 5, pady = 5)
    inputAMT_Entry = Entry(root, width = 20, textvariable = getAMT)
    inputAMT_Entry.grid(row = 1, column = 1, padx = 5, pady = 5)

    fromLabel = Label(root, text = "FROM:", bg = "darkolivegreen4")
    fromLabel.grid(row = 2, column = 0, padx = 5, pady = 5)
    root.fromCombo = ttk.Combobox(root, values = currencyList)
    root.fromCombo.grid(row = 2, column = 1, padx = 5, pady = 5)

    toLabel = Label(root, text = "TO:", bg = "darkolivegreen4")
    toLabel.grid(row=3, column = 0, padx = 5, pady=5)
    root.toCombo = ttk.Combobox(root, values = currencyList)
    root.toCombo.grid(row = 3, column = 1, padx = 5, pady = 5)

    convertButton = Button(root, text = "CONVERT", width = 25, command = Convert)
    convertButton.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)

    exrateLabel = Label(root, text = "EXCHANGE RATE:",bg = "darkolivegreen4")
    exrateLabel.grid(row = 5, column = 0, padx = 5, pady = 30)
    root.exchangerateLabel = Label(root, font = ('',20),bg = "darkolivegreen4")
    root.exchangerateLabel.grid(row = 5, column = 1, padx = 5, pady = 30)

    outputLabel = Label(root, text = "CONVERTED AMOUNT:", bg = "darkolivegreen4")
    outputLabel.grid(row = 6, column = 0,padx = 5, pady = 20)
    root.outputAMT_Label = Label(root, font = ('',20),bg = "darkolivegreen4")
    root.outputAMT_Label.grid(row = 6, column = 1, padx = 5, pady = 20)

# Defining Convert() function for converting the curreny
def Convert():
    # Fetching & storing user-inputs in resepective variables
    # Converting user-input amount which is a string into float type
    inputAmt = float(getAMT.get())
    fromCur = root.fromCombo.get()
    toCur = root.toCombo.get()

    # Storing the API Key from https://www.alphavantage.co/
    apiKey = "YOUR API KEY"
    # Storing the base URL
    baseURL = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    # Storing the complete URL
    inputURL = baseURL+"&from_currency="+fromCur+"&to_currency="+toCur+"&apikey="+apiKey

    # Sending the request to URL & Fetching and Storing the response in response variable
    response = requests.get(inputURL)
    # Returning the JSON object of the response and storing it in result
    result = response.json()
    print(json.dumps(result, indent=2))

    # Getting the exchange rate (Required Information)
    exchangeRate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
    # Displaying exchange rate in respective label after rounding to 2 decimal places
    root.exchangerateLabel.config(text=str(round(exchangeRate, 2)))

    # Calculating the converted amount and rounding the decimal to 2 places
    calculateAmt = round(inputAmt * exchangeRate, 2)
    # Displaying the converted amount in the respective label
    root.outputAMT_Label.config(text=str(calculateAmt))

# Creating object of tk class
root = tk.Tk()

# Setting title, background color & size of tkinter window
# & disabling the resizing property
root.geometry("400x350")
root.resizable(False, False)
root.title("PyCurrenyConverter")
root.config(bg = "darkolivegreen4")

# Creating tkinter variables
getAMT = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
