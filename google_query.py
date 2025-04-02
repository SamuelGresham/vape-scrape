# Makes a query to Google and returns the results

from dotenv import load_dotenv
import os
import requests
import pprint

# Returns 
load_dotenv()
google_search_api_secret = os.getenv("GOOGLE_SEARCH_SECRET")
google_search_cx = os.getenv("GOOGLE_SEARCH_CX")

def query(q):
    count = 0
    for i in range(9):
        res = requests.get("https://www.googleapis.com/customsearch/v1", params={
            "key": google_search_api_secret,
            "cx": google_search_cx,
            "q": q,
            "gl": "au",
            "start":str(10*(i+1))

        })
        if res.status_code != 200:
            print(res.url)
            raise Exception(f"Error {res.status_code}: {res.text}")
        else: 
            results = res.json()
            for item in results["items"]:
                print(item["title"])
                count += 1
    print(count)
            
              

query("Test")