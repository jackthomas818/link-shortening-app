import requests

# Set the API endpoint
api_url = "http://localhost:5000/link/shorten"

# Example long URL to be shortened
long_url = "https://www.example.com/some/long/url"

# Prepare the payload data
data = {"long_url": long_url}

# Send the POST request
response = requests.post(api_url, json=data)

# Print the response
if response.status_code == 201:
    shortened_link = response.json()
    print("Shortened URL:", shortened_link["short_url"])
else:
    print("Error:", response.status_code)
    print(response.json())
