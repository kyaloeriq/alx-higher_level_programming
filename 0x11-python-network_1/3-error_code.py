#!/usr/bin/python3
"""
script takes a URL as input, sends a request to the URL, and displays the body of the response
"""
import urllib.request
import urllib.error
import sys

def fetch_url(url):
    """
    Fetches the content of a URL and prints it.
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)


    url = sys.argv[1]
    fetch_url(url)
