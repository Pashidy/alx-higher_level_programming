#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file in the body, and displays the response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
