
import requests

url = 'http://jsonplaceholder.typicode.com/posts/1'
jsonPayload =  {'userId':1, 'id':200, 'title':'test title for testing', 'body':'This is a sample testing.bvbvgfihgj cfsoigsh nhdkfhshgkh dnfkjsgkgnbg gsgsggs'}

response = requests.put(url,json=jsonPayload)

print(response.json())