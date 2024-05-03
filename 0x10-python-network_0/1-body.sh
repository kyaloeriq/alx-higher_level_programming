#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -w "%{http_code}" -o response.txt $1 | tail -n 1 | grep -q "200" && cat response.txt
