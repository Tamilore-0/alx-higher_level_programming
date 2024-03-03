#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the 
URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import sys

url = sys.argv[1]

req = urllib.request.Request(url)
try:
	with urllib.request.urlopen(req) as response:
		content = response.read().decode('utf-8')
		print(content)
except Exception as e:
	print(f"Error code: {e.code}")
