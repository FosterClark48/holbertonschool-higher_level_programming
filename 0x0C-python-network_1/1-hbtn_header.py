#!/usr/bin/python3
"""
Script that takes URL as input, sends a request to the URL,
and displays the value of the X-Request-Id found in header of the response
"""
import urllib.request
import sys

"""Ensure code is only executed if script is run directly"""
if __name__ == '__main__':
    """Retrieve URL argument passed to script"""
    url = sys.argv[1]
    """
    Ensure response is properly closed.
    Open URL with urlopen() and store in response variable
    """
    with urllib.request.urlopen(url) as response:
        """
        Use getheader on response object to retrieve value of X-Request-Id.
        Print X-Request-Id value
        """
        print(response.getheader('X-Request-Id'))
