# impots
import requests
import json
from datetime import datetime

# Target
SUBREDDIT = 'wallstreetbets'
FROM = 1606436515
TO = '1669335715'
NUM_POSTS = '1000'
SEC_PER_DAY = 86400

URL = f"https://api.pushshift.io/reddit/search/submission/?subreddit={SUBREDDIT}&sort=desc&sort_type=created_utc&after={FROM}&before={TO}&size={NUM_POSTS}"

######################################################################
# Fetch data
######################################################################
posts = list()
counter = 0
while True:
    # Fetches data from pushshift.io and converts it to json
    temp_res = requests.get(URL).json()['data'] 
    
    #create new dictionary:
    temp_data = list()
    for i in range(len(temp_res)):
        temp_data.append({
            "title":temp_res[i]['title'],
            "created_utc":temp_res[i]['created_utc']
        })
        
    # Add datapoints to list of posts
    posts += temp_data
    if counter % 20 == 0:
        # Save Progress
        with open('wsb_data.json', 'w') as f:
            json.dump({"data":posts}, f)
    
    # Find oldest data from this fetch
    temp_dates = set()
    for i in range(len(temp_res)):
        temp_dates.add(temp_res[i]['created_utc'])
        
    # Check if we have all the datapoint we need
    if min(temp_dates) <= FROM+SEC_PER_DAY:
        break
    URL = f"https://api.pushshift.io/reddit/search/submission/?subreddit={SUBREDDIT}&sort=desc&sort_type=created_utc&after={FROM}&before={min(temp_dates)}&size={NUM_POSTS}"
    if counter % 20 == 0:
        print(f"Counter: {counter}")
        print(f"Min Date: {datetime.fromtimestamp(int(min(temp_dates)))}")
        
    counter +=1
print("DONE!")