import requests
from bs4 import BeautifulSoup

# Specify the url of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/IBM'

# Send an HTTP GET request to the webpage
response = requests.get(url)

# Store the HTML content in a variable
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content,'html.parser')

# Create a BeautifulSoup object to parse the HTML
print(html_content[:500])

# Find all <a> tags(anchor tags) in the html
links = soup.find_all('a')
# Iterate through the list of links and print their text
for link in links:
    print(link.text)