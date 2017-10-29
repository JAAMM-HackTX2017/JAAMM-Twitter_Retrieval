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

# saves oauth_token and oauth_token_secret
# ACESS_TOKEN= twitter.obtain_access_token()
# print(ACESS_TOKEN)

# OAUTH_TOKEN = auth['oauth_token']
# OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

# twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

## final_step = twitter.get_authorized_tokens(oauth_verifier)

# OAUTH_TOKEN = final_step['oauth_token']
# OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']




# print(auth['auth_url'])

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
    results[i + offset] = [entry['text'], [random.uniform(30.0, 50.0), random.uniform(70.0, 125.0)]]
if 'size' in results:
    results["size"] += len(entries)
else:
    results["size"] = len(entries)



with open(POSTS_FILE, 'w') as outfile: 
        json.dump(results, outfile)
