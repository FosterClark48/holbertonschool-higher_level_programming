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
    Open URL with requests.get() and store in response variable
    """
    response = requests.get(url)
    """
    Use headers property of response object to access headers.
    Use get() method to retrieve value of X-Request-Id.
    Print X-Request-Id value
    """
    print(response.headers.get('X-Request-Id'))
