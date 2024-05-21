#!/usr/bin/python3
"""
Script that takes a URL and an email, sends a POST request to the passed URL
"""

import urllib.request
import urllib.parse
import sys


def main():
    """
    Sends a POST request to the provided URL with the email as a parameter
    """
    url = sys.argv[1]  # Get the URL from the command-line arguments
    email = sys.argv[2]  # Get the email from the command-line arguments

    # Prepare the data for the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Use a with statement to open the URL and send the POST request
    with urllib.request.urlopen(url, data) as response:
        # Read the response content
        response_body = response.read()

    # Decode the response body to utf-8
    utf8_content = response_body.decode('utf-8')

    # Print the decoded response body
    print(utf8_content)


if __name__ == "__main__":
    main()
