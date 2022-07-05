import requests
import twitter

response = requests.get("https://twitter.com/home")
print(response.json())