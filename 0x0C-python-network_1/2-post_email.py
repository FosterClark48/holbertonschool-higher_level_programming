#!/usr/bin/python3
"""
Script that takes a URL and email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

"""Ensure code is only executed if script is run directly"""
if __name__ == '__main__':
    """Get the URL and email from command-line arguments"""
    url = sys.argv[1]
    email = sys.argv[2]

    """Encode email as URL parameter"""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    """
    Create Request object the represents POST request to be sent to
    specified URL and assign it to req variable
    """
    req = urllib.request.Request(url, data=data, method='POST')
    """
    Ensure response is properly closed.
    Send POST request and get response object in response variable
    """
    with urllib.request.urlopen(req) as response:
        """
        Use getheader on response object to retrieve value of X-Request-Id.
        Print X-Request-Id value
        """
        print(response.read().decode('utf-8'))
