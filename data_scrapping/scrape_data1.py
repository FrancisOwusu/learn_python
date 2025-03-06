import os 
import requests
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)
# get request status code
r.status_code
# view the request headers:
r.request.headers
# view request body
print("request body:", r.request.body)

header=r.headers
r.headers
# obtain request date
header['date']
# obtain request content type
header['Content-Type']

# check the encoding:
r.encoding

r.text[0:100]

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)
print(r)
print(r.headers)
r.headers['Content-Type']

path=os.path.join(os.getcwd(),'image.png')
print(path)
with open(path,'wb') as f:
    f.write(r.content)
    
# view the image
Image.open(path)