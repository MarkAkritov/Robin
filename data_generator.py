import numpy as np
from datetime import datetime
from pprint import pprint
import json

emotions = {
    "happy":    0, 
    "sad":  0, 
    "fear":     0, 
    "angry":    0, 
    "disgust":      0, 
    "surprise": 0, 
    "neutral":  0
}

data = {}
timestamp = 1566998321
for i in range(1, 100):
    arr = np.array([i,
                    100 - i,
                    np.random.randint(2, size=1),
                    np.random.randint(2, size=1),
                    np.random.randint(2, size=1),
                    np.random.randint(2, size=1),
                    np.random.randint(2, size=1)])
    arr = arr/sum(arr)
    emotions = {}
    emotions["angry"] = arr[0]
    emotions["happy"] = arr[1]
    emotions["fear"] = arr[2]
    emotions["sad"] = arr[3]
    emotions["disgust"] = arr[4]
    emotions["surprise"] = arr[5]
    emotions["neutral"] = arr[6]
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

with open("scenario_happy_sad.json", "w") as file:
    json.dump(data, file)