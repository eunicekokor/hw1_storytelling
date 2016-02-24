import requests
import redis
import time
import numpy
import json
import sys
from TwitterAPI import TwitterAPI

access_token_key = "28203065-AzK05fKKF4OzmPE0m1PbdZTq0vj4lsogO8JXWxXLH"
access_token_secret = "q6j4iDDMqbsiY3LJTZXd1SCQ1RHgNZTQbQw1tcwpO9LDO"
consumer_secret = "b6eIYasgVwIu3cskn3a8omPwms5S216i2G9OaBURYRQCFSM9Rd"
consumer_key = "sXYl8MLLMnfE7HCl9lIZ3ytEl"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
conn = redis.Redis()

last = 0
while True:
    TERM = 'rain'
    NYC = '-74,40,-73,41'
    print "searching for {} in NYC".format(TERM)
    r = api.request('statuses/filter', {'track': TERM, 'locations':NYC})
    for item in r:
      d = {"time": time.time(), "tweet": str(item["text"].encode('utf-8')), "created_at": str(item["created_at"].encode('utf-8'))}
      # print d

      if last == 0:
          last = d["time"]
          continue

      delta = d["time"] - last
      # print {"time": d["time"], "delta": delta}
      conn.setex(d["time"], delta, 5)
      keys = conn.keys()

      values = conn.mget(keys)

      try:
          deltas = [float(v) for v in values]
      except TypeError:
          print keys
          continue

      if len(deltas):
        rate = sum(deltas)/float(len(deltas))
      else:
        rate = 0


      d["rate"] = rate


      # print json.dumps({"rate":rate})
      if rate <= .17:
        print "the {} is really exciting people right now!".format(TERM)
        d["exciting"] = True

      last = d["time"]

      sys.stdout.flush()

    delta_t = numpy.random.exponential(5)
    time.sleep(delta_t)
