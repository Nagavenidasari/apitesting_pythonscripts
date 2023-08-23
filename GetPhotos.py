import requests

url = 'https://jsonplaceholder.typicode.com/photos'

# get the data about the photos
response=requests.get(url)

#get response
json_data = response.json()

#print the response
#print(json_data)
print(response.status_code)
