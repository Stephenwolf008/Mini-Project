import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.brainyquote.com/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'lxml')
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Authors', 'Quotes'])
author = soup.find_all('a', "bq_on_link_cl")
for link in author:
    linkText = "https://www.brainyquote.com/" +link.get('href')
    print(link.text)
    r1 = requests.get(linkText)
    soup1 = BeautifulSoup(r1.content, 'lxml')
    quote = soup1.find_all('a', "oncl_q")
    for img in quote:
        csv_writer.writerow([link.text,img.text])
csv_file.close()

