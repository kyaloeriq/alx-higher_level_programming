#!/bin/bash
# Sends a request to the provided URL and gets the size of the response body
curl -sI "$1" | awk '/Content-Length/ {print $2}'
