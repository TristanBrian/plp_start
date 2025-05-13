import requests

# This script demonstrates how to use the requests library to make a GET request to a public API
# and print the response in JSON format.
# Import the requests library

response = requests.get('https://api.github.com/events')
print(response.json())

