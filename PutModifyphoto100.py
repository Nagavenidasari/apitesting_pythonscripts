import requests

url = 'https://jsonplaceholder.typicode.com/photos/100'
jsonPayload={'albumId':1, 'title':'test', 'url':'nothing.com','thumbnailUrl':'nothing.com'}

response=requests.put(url,json=jsonPayload)

print(response.json())
print(response.status_code)