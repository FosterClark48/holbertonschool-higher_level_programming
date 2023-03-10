#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API
"""
import requests
import sys

"""Allow script to be imported w/out execution of main code"""
if __name__ == '__main__':
    """Set up API endpoint and authentication credentials"""
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits?per_page=10'.format(
        owner, repo)

    """Make a GET request to API endpoint w/ repo and owner"""
    response = requests.get(url)
    """extract JSON data from response obj and store in commits var"""
    commits = response.json()
    """Iterate over commits list and assign each iteration to 'commit' var"""
    for commit in commits:
        """
        Extract SHA-1 hash of the commit from JSON data
        in 'commit' dict & assign to 'sha' var
        """
        sha = commit['sha']
        """
        Extract the name of the author of the commit from JSON data
        in 'commit' dict and assign it to 'author_name' var
        """
        author_name = commit['commit']['author']['name']
        print('{}: {}'.format(sha, author_name))
