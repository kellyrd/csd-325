# Kelly Dimick
# Assignment 9.2
# 11/05/2026

# Purpose: Retrieve astronaut data from an API and display the response in formatted JSON.

# Source: Dataquest, "How to use an API in Python" (https://www.dataquest.io/blog/python-api-tutorial/)

import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)
print(response.json())

jprint(response.json())