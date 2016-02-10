#!/usr/bin/env python
from sys import stdout
import requests
import json
import datetime
import time
stock_data = {"quote": None}

def has_changed(initial, current):
  if initial != current:
    return True
  else:
    return False
while True:
    now = datetime.datetime.now()
    # Define which stock I would like to analyze
    stock = "FB"
    stock_url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?Symbol={}".format(stock)
    r2 = requests.get(stock_url)
    stock_results = r2.json()

    if not stock_data["quote"]:
      stock_data["quote"] = stock_results['LastPrice']
      print "{}: ${}".format(now, stock_data["quote"])

    if has_changed(stock_results['LastPrice'], stock_data["quote"]):
      stock_data["quote"] = stock_results['LastPrice']
      print "{}: ${}".format(now, stock_data["quote"])
    stdout.flush()

    time.sleep(5)
