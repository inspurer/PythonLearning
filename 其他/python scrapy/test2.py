import requests
from lxml import etree

url = 'https://book.douban.com/top250'
data = requests.get(url).text
s=etree.HTML(data)

file=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a/@title')
for title in file:
    print(title)
