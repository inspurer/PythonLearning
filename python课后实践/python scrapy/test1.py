import requests
from lxml import etree

url = 'https://movie.douban.com/subject/1292052/'
data = requests.get(url).text
s=etree.HTML(data)

film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
print(film)