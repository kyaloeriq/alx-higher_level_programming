#!/bin/bash
# Sends a POST request to the provided URL with email and subject variables
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
