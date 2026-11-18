import requests 

#API endpoint
url = "https://jsonplaceholder.typicode.com/posts/2"

#send GET request
response = requests.get(url)

#check response status
print(response.status_code)

#convert response to python dictionary
data = response.json()

#display returned information
print(data)
