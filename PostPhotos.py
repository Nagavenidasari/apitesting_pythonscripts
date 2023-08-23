import requests

url = 'https://jsonplaceholder.typicode.com/photos'
jsonPayload={'albumId':1, 'title':'test', 'url':'nothing.com','thumbnailUrl':'nothing.com'}
response=requests.post(url,json=jsonPayload)
print(response.status_code)
print(response.json())
