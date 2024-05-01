#!/bin/bash
# Sends a GET request to the provided URL with a custom header X-School-User-Id

curl -X GET -H "X-School-User-Id: 98" "$1"
