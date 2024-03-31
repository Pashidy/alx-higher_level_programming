#!/bin/bash
# This script takes a URL as input and displays all HTTP methods the server will accept
curl -sI "$1" | grep -i Allow | awk '{print $2}'

