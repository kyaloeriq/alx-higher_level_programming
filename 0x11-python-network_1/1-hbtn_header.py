#!/usr/bin/python3
"""
Python script that takes in a URL, sends request to the URL, displays value of the X-Request-Id variable found in the response.
"""

import urllib.request
import sys


def main():
    """
    Sends a request to the URL, prints value of the X-Request-Id variable in the header of the response.
    """
    url = sys.argv[1]  # Get the URL from the command-line arguments

    # Use a with statement to open the URL
    with urllib.request.urlopen(url) as response:
        # Get the headers from the response
        headers = response.getheaders()
        # Convert headers to a dictionary for easy access
        headers_dict = dict(headers)
        # Get the value of 'X-Request-Id' from the headers
        x_request_id = headers_dict.get('X-Request-Id')

    # Print the value of the X-Request-Id header
    print(x_request_id)


if __name__ == "__main__":
    main()
