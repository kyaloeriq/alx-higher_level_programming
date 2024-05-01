#!/bin/bash
# sends DELETE request using curl and displays response body
curl -X DELETE -s -o response_body.txt -w "%{http_code}" "$1" && cat response_body.txt
