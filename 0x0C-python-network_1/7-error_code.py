#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response
using requests package instead of urllib
"""
import requests
import sys

"""Ensure code is only executed if script is run directly"""
if __name__ == '__main__':
    """Get the URL from command-line arguments"""
    url = sys.argv[1]

    try:
        """Send a GET request to the URL and get the response"""
        response = requests.get(url)
        """Raise an exception for any HTTP error status codes"""
        response.raise_for_status()
        """Print response body to console, decoded as utf-8"""
        print(response.content.decode('utf-8'))
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
