#!/bin/bash
# sends DELETE request using curl and display response body
curl -X DELETE -i "$1" | sed '1,/\r\{0,1\}$/d'
