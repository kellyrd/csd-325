# Kelly Dimick
# Assignment 9.2
# 11/05/2026

# Purpose: Retrieve user data from an API and display the response in formatted JSON.

# Source: Dataquest, "How to use an API in Python" (https://www.dataquest.io/blog/python-api-tutorial/)

import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
response = requests.get("https://jsonplaceholder.typicode.com/users") 

print(response.status_code)
print(response.json())
jprint(response.json())