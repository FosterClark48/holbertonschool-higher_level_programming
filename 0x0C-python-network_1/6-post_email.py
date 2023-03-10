#!/usr/bin/python3
"""
Script that takes a URL and email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
only using requests and sys packages
"""
import requests
import sys

"""Ensure code is only executed if script is run directly"""
if __name__ == '__main__':
    """Get the URL and email from command-line arguments"""
    url = sys.argv[1]
    email = sys.argv[2]

    """Create dictionary w/ email parameter"""
    data = {'email': email}

    """Send a POST request to the URL with the email parameter"""
    response = requests.post(url, data=data)

    """Display the body of the response"""
    print(response.text)
