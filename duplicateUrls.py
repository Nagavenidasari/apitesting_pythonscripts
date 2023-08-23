
import requests

url = 'https://jsonplaceholder.typicode.com/photos'

#get the data about the photos
response = requests.get(url)

#read the data in to a variable json_data
json_data= response.json()

# create an empty list to store the url of each photo
url_list=[]


for photo in json_data:
    url_list.append(photo['url'])

# get the lenght of the list
print(len(url_list))

#create a set to elimate the duplicate in the list

new_urllist = set(url_list)

print(len(new_urllist))

duplicate_urls = len(url_list) - len(new_urllist)

print("Number of duplicate URL's:",duplicate_urls)