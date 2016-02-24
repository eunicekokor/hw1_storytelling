# Programming Assignment #2

## Part 1: The Data Stream: Mentions of Weather in New York City
The stream I created is based upon the Tweets originating in New York City and mention the text 'weather' from Twitter, a social media platform that provides user generated <140 character blurbs in realtime.

**API Used:** [Twitter API]() through Python wrapper [TwitterAPI](https://github.com/geduldig/TwitterAPI) If you would like more information on TwitterAPI, the docs and other usage info is available at [https://github.com/geduldig/TwitterAPI](https://github.com/geduldig/TwitterAPI)

Every five seconds, I query this API for the current stock price of Facebook, Inc. which is an online social networking platform and service that has been operating since 2004. Because this API returns information at the current time, I wanted the stream the following:

1. The initial price at the time the stream is opened
  Basically, if we want to see how the Facebook stock price is changing throughout the day (or whatever length of time we want to analyze) a starting point is important.
2. The exact time that that price was fetched.
  If someone analyzing my stream needed to fact check or saw a one second discrepency, it would be important to document the time in which my stream parsed this assumed live data.
3. An output reflecting changed prices.
  This is important for the following reasons:
  - a. The stock market opens and closes at approximately 9:30am and 4:00pm respectively, so my stream won't output more than one result (supposedly if there are no fluctuations before or after those times) before 9:30am or after 4:00pm.
  - b. I only wanted to reflect the changing nature of the stock market, so my stream is an accurate representation of what is happening in real life with the stocks within 5 seconds.

## Instructions to Test this Stream:
To test this stream you need to utilize two terminal windows:

**Terminal #1:** `cd` into this directory, run `websocketd --port=8000 --staticdir=. ./hw1.py`
####What Does This Do?
This creates the stream of data through which I've already parsed from an API and outputs to `stdout` what I described above. Our output is now a websocket on port 8000.

**Terminal #2:** `cd` into this directory, run `python -m SimpleHTTPServer 8080`
####What Does This Do?
This hosts the html page which has a script to connect to the websocket on port 8000 that we just created above!

###Viewing Results
type in `localhost:8080` after completing the above to view the html page and see the live output of the stream
