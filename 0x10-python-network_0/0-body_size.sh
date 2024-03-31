#!/bin/bash
# This script takes a URL as input, sends a request to that URL using curl, and displays the size of the body of the response in bytes
curl -s "$1" | wc -c
