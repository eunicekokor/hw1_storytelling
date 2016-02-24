# Programming Assignment #2

## Part 1: The Data Stream: Mentions of Weather in New York City
The stream I created is based upon the Tweets originating in New York City and mention the text 'weather' from Twitter, a social media platform that provides user generated <140 character blurbs in realtime.

I have always wondered if other people tweeted about the weather if there was something significant happening. I know definitely do. So, I wanted a stream that created an alert when a large number of people in a certain area are frantically tweeting at a certain rate about this weather event. Maybe this could signal a catastrophe? Anyway, a bot like this could be useful just like LA's earthquake bot, or something like that, to corroborate data from weather service centers about potentially hazardous conditions.

This webpage shows the most recent tweet. If the tweet appears during an exciting time, the tweet is accompanied by the words "Exciting Weather". That way you know if that tweet is corollated with an exciting period of time for weather in that area.

My alerting system is when the rate goes above .17. Why? It is mostly arbitrary. I did see, however, that there weren't a lot of 'exciting' weather events when the average rates were above .17, so I set a baseline after looking at many different rates over the course of time.

**API Used:** [Twitter API](https://apps.twitter.com/) through Python wrapper [TwitterAPI](https://github.com/geduldig/TwitterAPI) If you would like more information on TwitterAPI, the docs and other usage info is available at [https://github.com/geduldig/TwitterAPI](https://github.com/geduldig/TwitterAPI).

## Instructions to Test this Stream:
To test this stream you need to utilize two terminal windows:
**Terminal #1:** `cd` into this directory, run `redis-server`
####What Does This Do?
This creates a Redis server so we can store our time-deltas and be able to calculate rate!

**Terminal #2:** `cd` into this directory, run `websocketd --port=8000 --staticdir=. ./hw2.py`
####What Does This Do?
This creates the stream of data through which I've already parsed from an API and outputs to `stdout` what I described above. Our output is now a websocket on port 8000.

**Terminal #3:** `cd` into this directory, run `python -m SimpleHTTPServer 8080`
####What Does This Do?
This hosts the html page which has a script to connect to the websocket on port 8000 that we just created above!

###Viewing Results
type in `localhost:8080` after completing the above to view the html page and see the live output of the stream
