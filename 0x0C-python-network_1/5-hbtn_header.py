#!/usr/bin/python3
"""
Script that takes URL as input, sends a request to the URL,
and displays the value of the X-Request-Id found in header of the response
only using the requests and sys packages
"""
import requests
import sys

"""Ensure code is only executed if script is run directly"""
if __name__ == '__main__':
    """Retrieve URL argument passed to script"""
    url = sys.argv[1]
    """
    Ensure response is properly closed.
    Open URL with requests.get() and store in response variable
    """
    with requests.get(url) as response:
        """
        Use headers property of response object to access headers.
        Use get() method to retrieve value of X-Request-Id.
        Print X-Request-Id value
        """
        print(response.headers.get('X-Request-Id'))
