import numpy as np
from datetime import datetime
from pprint import pprint
import json

emotions = {
    "happy":    0, 
    "sad":  	0, 
    "fear":     0, 
    "angry":    0, 
    "disgust":  0, 
    "surprise": 0, 
    "neutral":  0
}

data = {}
timestamp = 1566998321
count = 100
for i in range(1, count):
    arr = np.array([i,			# less prob
                    count - i,	# high prob
                    np.random.randint(2, size=1),
                    np.random.randint(2, size=1),
                    np.random.randint(2, size=1),
                    np.random.randint(2, size=1),
                    np.random.randint(2, size=1)])
    arr = arr/sum(arr)
    emotions = {}
    emotions["happy"] = float(arr[0])     # less prob
    emotions["neutral"] = float(arr[1])   # high prob
    emotions["fear"] = float(arr[2])
    emotions["surprise"] = float(arr[3])
    emotions["sad"] = float(arr[4])
    emotions["disgust"] = float(arr[5])
    emotions["angry"] = float(arr[6])
    #pprint(emotions)
    data[str(datetime.fromtimestamp(timestamp))] = {}
    data[str(datetime.fromtimestamp(timestamp))]["person"] = {}
    data[str(datetime.fromtimestamp(timestamp))]["person"]["face"] = {}
    data[str(datetime.fromtimestamp(timestamp))]["person"]["text"] = {}
    data[str(datetime.fromtimestamp(timestamp))]["person"]["face"]["emotions"] = {}
    data[str(datetime.fromtimestamp(timestamp))]["person"]["text"]["emotions"] = {}
    data[str(datetime.fromtimestamp(timestamp))]["person"]["face"]["emotions"] = emotions
    data[str(datetime.fromtimestamp(timestamp))]["person"]["text"]["emotions"] = emotions

    timestamp += 1

with open("scenario_neutral_happy.json", "w") as file:
    json.dump(data, file)