#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -D - "$1" | awk '/^HTTP/{c=$2} END{print c~/^3/?(c~/^30[0-9]$/?"5 redirection with multiple status code":"1 redirection"):"No redirection"}'
