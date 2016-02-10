# Programming Assignment #1

## Part 1: The Data Stream: Facebook Price
**API Used:** (dev.markitondemand.com)[dev.markitondemand.com]'s Stock Quote API, which is an API that allows anyone to see the current value of a company's stock for companies traded on the BATS Exchange, also known as "Better Alternative Trading System". When querying for a company's current stock, it returns a lot of additional information, including the volume of the stock, the change (both by % and number) since the previous day's close and more information.


## Instructions to Test this Stream:
To test this stream you need to utilize two terminal windows:
**Terminal #1:** `cd` into this directory, run `websocketd --port=8000 --staticdir=. ./hw1.py`
###What Does This Do?
This creates the stream of data through which I've already parsed from an API

**Terminal #2:** `cd` into this directory, run `python -m SimpleHTTPServer 8080`

