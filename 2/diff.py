import json
import simplejson as js
import sys

last = 0
while True:
    line = sys.stdin.readline()
    d = js.loads(line, encoding='utf-8')


    if last == 0:
        last = d["time"]
        continue

    delta = d["time"] - last

    print json.dumps({"t": d["time"], "delta": delta})
    last = d["time"]
