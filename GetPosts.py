
import requests

url = 'http://jsonplaceholder.typicode.com/posts'

response = requests.get(url)


print(response.json())
