import requests

response = requests.get('http://localhost:5000/hello/World')
response.json()
print(response.status_code)
print(response.json())