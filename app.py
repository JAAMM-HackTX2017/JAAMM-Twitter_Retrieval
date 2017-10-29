from twython import Twython
from twython import TwythonStreamer
import json
import random
import os.path



"""
Talk to Twitter and give them my Consumer Key  and Consumer Secret
"""

secretFile = open("./secret.txt", "r")
consumerSecrets = []
POSTS_FILE = "posts.json"

for secret in secretFile:
    consumerSecrets.append(secret.strip())

# print(consumerSecrets)

APP_KEY = consumerSecrets[0]
APP_SECRET = consumerSecrets[1]
ACCESS_TOKEN =consumerSecrets[2] 

twitter = Twython(APP_KEY, access_token= ACCESS_TOKEN)

search_results = twitter.search(q='flooding')

#check to see if file that stores posts exists in current directory as this script
if os.stat(POSTS_FILE).st_size != 0 and os.path.isfile(POSTS_FILE):
    # retrieve previously collected data
    with open(POSTS_FILE) as json_data:
        results = json.load(json_data)
    offset = results["size"]
else:
    results = {}
    offset = 0

entries = search_results['statuses']
for entry,i in zip(entries, range(len(entries))):
    # print(entry)
    results[i + offset] = [entry['text'], [random.uniform(20.0, 40.0), random.uniform(70.0, 90.0)]]
if 'size' in results:
    results["size"] += len(entries)
else:
    results["size"] = len(entries)

results["region-size"] = 20
results["quadrant-size"] = 2

with open(POSTS_FILE, 'w') as outfile: 
        json.dump(results, outfile)
