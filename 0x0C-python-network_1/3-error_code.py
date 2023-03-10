#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
import urllib.request
import urllib.error
import sys

"""Ensure code is only executed if script is run directly"""
if __name__ == '__main__':
    """Get the URL from command-line arguments"""
    url = sys.argv[1]

    try:
        """Open URL and read its contents"""
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
