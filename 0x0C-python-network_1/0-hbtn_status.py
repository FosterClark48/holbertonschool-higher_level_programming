#!/usr/bin/python3
"""Script that fetches status of https://intranet.hbtn.io/status"""
import urllib.request

"""Set URL to fetch"""
url = 'https://intranet.hbtn.io/status'
"""
Use with statement to manage network connection to ensure proper cleanup
"""
with urllib.request.urlopen(url) as response:
    """Read response from network connection into body variable"""
    body = response.read()

print('Body response:')
print('\t- type: {}'.format(type(body)))
print('\t- content: {}'.format(body))
print('\t- utf8 content: {}'.format(body.decode('utf-8')))
