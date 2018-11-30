import requests
from lxml import etree

url = 'https://book.douban.com/top250'
data = requests.get(url).text
s=etree.HTML(data)

title=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a/@title')
nums=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[2]/text()')
for i in range(25):
    print("书名:{}  得分 :{}".format(title[i],nums[i]))
