#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == '__main__':
    """Set up API endpoint and authentication credentials"""
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    """Make a GET request to API endpoint w/ auth creds"""
    response = requests.get(url, auth=(username, password))

    """Check if response was successful"""
    if response.status_code == 200:
        """Retrieve value of id key from JSON response returned by API call"""
        user_id = response.json()['id']
        print(user_id)
    else:
        """Display None if response wasn't successful"""
        print(None)
