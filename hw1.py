#!/usr/bin/env python
from sys import stdout
import requests
import json
import datetime
import time

''' This dictionary, stock_data will be where we will eventually store
the current stock value '''
stock_data = {"quote": None}

''' This function checks if the value we have for the current stock price has
changed from the value we have stored in our dictionary'''
def has_changed(initial, current):
    if initial != current:
        return True
    else:
        return False

while True:
    now = datetime.datetime.now()  # Getting the current time so we can output it
    stock = "FB"  # Define which stock I would like to analyze
    # API url asking for response in json format
    stock_url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?Symbol={}".format(stock)

    r2 = requests.get(stock_url)  # Capturing the response from the API
    stock_results = r2.json()  # Parsing the API response in a more-readable JSON format

    # This comparison checks if we already have a value for the current price
    # This helps us get the initial value of the stock so we can
    # check if it has changed
    if not stock_data["quote"]:
      stock_data["quote"] = stock_results['LastPrice']
      print "{}: ${}".format(now, stock_data["quote"])

    # using the changed stock and replacing our dictionary with the changed price
    if has_changed(stock_results['LastPrice'], stock_data["quote"]):
      stock_data["quote"] = stock_results['LastPrice']
      print "{}: ${}".format(now, stock_data["quote"])
    stdout.flush()

    # Waiting 5 seconds to re-do
    time.sleep(5)
