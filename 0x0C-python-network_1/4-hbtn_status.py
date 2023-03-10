#!/usr/bin/python3
"""
Script that fetches status of https://intranet.hbtn.io/status
using requests package
"""
import requests

"""Set URL to fetch"""
url = 'https://intranet.hbtn.io/status'
"""
Send a GET request to the URL & store
the response in the response variable
"""
response = requests.get(url)

print('Body response:')
print('\t- type: {}'.format(type(response.text)))
print('\t- content: {}'.format(response.text))
