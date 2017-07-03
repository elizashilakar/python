import requests
import csv  
from datetime import datetime  

from bs4 import BeautifulSoup

f = open('index.csv', 'w')
writer = csv.writer(f)
page = requests.get("http://healthmandu.com")
soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all('strong')
writer.writerow(['Title'])

for title in data:
    name = title.get_text()
    writer.writerow([name])
