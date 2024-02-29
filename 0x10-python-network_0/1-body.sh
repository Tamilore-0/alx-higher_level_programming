#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# Send a GET request to the URL and store the response body in a variable
response=$(curl -sL -w "%{http_code}" -o /dev/null "$1")

if [[ $response != 4* && $response != 5* ]]; then
	# display the body
	curl -sL "$1"
fi
