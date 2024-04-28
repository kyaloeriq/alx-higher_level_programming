#!/bin/bash
# Sends a request to the provided URL and gets the size of the response body
response=$(curl -sI "$1" | grep -i '^content-length:' | tr -d '[:space:]' | cut -d ':' -f 2)
