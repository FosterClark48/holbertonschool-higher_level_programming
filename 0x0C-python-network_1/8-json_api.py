#!/usr/bin/python3
"""
Script script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

"""
Check if one command line argument was provided
and set it as the value of q
"""
if len(sys.argv) == 2:
    q = sys.argv[1]
else:  # set q to an empty string
    q = ""

"""
Send a POST request to the search_user endpoint
with the q parameter set to the value of q
"""
response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

try:
    """Try and parse the response body as JSON"""
    data = response.json()
    if data:
        """If JSON object exists, print id and name in desired format"""
        print("[{}] {}".format(data["id"], data["name"]))
    else:
        """If JSON object is empty, print 'No result'"""
        print("No result")
except ValueError:
    """if parsing fails, print 'Not a valid JSON'"""
    print("Not a valid JSON")
