import os 
import requests,response
from PIL import Image
from IPython.display import IFrame

# Question: Download a file
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
    
url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}

# passing the dictionary payload to the params parameter of the  get() function:
r=requests.get(url_get,params=payload)
# We can print out the URL and see the name and values.
r.url
print("request body:", r.request.body)
print(r.text)
r.json()
r.json()['args']

# Post Requests
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
#print("POST request URL:",response.url )
#print("GET request URL:",r.url)
print("POST request URL:", r_post.url)  # Use r_post instead of response
print("POST request body:",response.request.body)
print("GET request body:",r.request.body)