#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the 
URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import sys
import urllib.error

url = sys.argv[1]

req = urllib.request.Request(url)
try:
	with urllib.request.urlopen(req) as response:
		content = response.read().decode('utf-8')
		print(content)
except urllib.error.HTTPError as e:
	print(f"Error code: {e.code}")
