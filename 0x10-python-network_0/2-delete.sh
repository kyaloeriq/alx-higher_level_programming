#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -X DELETE -s -o response_body.txt -w "%{http_code}" "$1" && cat response_body.txt | sed 's/000//g' && echo ""
