#!/usr/bin/env python
from sys import stdout
import requests
import json
import datetime
import time
weather_data = {}

def has_changed(initial, current, query, units):
  if initial != current:
    print "{}: The {} is {}{}.".format(datetime.datetime.now(), query, current, units)
    return True
  else:
    return False
while True:
    # get the citibike response from their API
    # api_key = "7240f211da7c1e42387d192d8405b523"
    # city_id = "5128581"
    # api_gold = "44db6a862fba0b067b1930da0d769e98"
    # url = ("http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=imperial").format(city_id, api_gold)
    # r = requests.get(url)
    # # extract my favourite citibike station
    # result = r.json()
    # stock = "FB,TSLA,AMZN"
    stock = "FB"
    stock_url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?Symbol={}".format(stock)
    r2 = requests.get(stock_url)

    stock_results = r2.json()
    print stock_results['LastPrice']
    stdout.flush()

    time.sleep(5)
