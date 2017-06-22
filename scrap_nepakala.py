from bs4 import BeautifulSoup

import requests

r  = requests.get("http://www.nepakala.com")

data = r.text

soup = BeautifulSoup(data, "html.parser")
print(soup.title.string)
print(soup.get_text())
for link in soup.find_all('a'):
    print(link.get('href'))