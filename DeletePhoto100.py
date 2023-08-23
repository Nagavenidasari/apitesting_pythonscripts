
import requests

url = 'https://jsonplaceholder.typicode.com/photos/100'
response=requests.delete(url)
print(response.json())
print(response.status_code)