#!/bin/bash
# This script takes a URL as input, sends a GET request to that URL using curl, and displays the body of the response if the status code is 200
curl -s -o /dev/null -w "%{http_code}\n" "$1" | grep -q 200 && curl -s "$1"

