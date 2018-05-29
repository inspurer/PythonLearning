from lxml import etree
import requests
import time

with open(r'E:\Python\python scrapy\xiaozhu.csv','w',encoding='utf-8') as f:
    for a in range(1,6):
        url = 'http://cd.xiaozhu.com/search-duanzufang-p{}-0/'.format(a)
        data = requests.get(url).text

        s=etree.HTML(data)
        file=s.xpath('//*[@id="page_list"]/ul/li')
        time.sleep(3)
    
        for div in file:
            title=div.xpath("./div[2]/div/a/span/text()")[0]
            price=div.xpath("./div[2]/span[1]/i/text()")[0]
            scrible=div.xpath("./div[2]/div/em/text()")[0].strip()
            pic=div.xpath("./a/img/@lazy_src")[0]
            
            f.write("{},{},{},{}\n".format(title,price,scrible,pic))