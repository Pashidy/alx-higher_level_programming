#!/bin/bash
# This script takes a URL as input, sends a GET request to that URL using curl, and displays the body of the response if the status code is 200
curl -sL "$1"
