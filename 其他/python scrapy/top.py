from lxml import etree
import requests
import time

with open(r'C:\Users\lenovo\Desktop\python学习\python课后实践\python scrapy\xiaozhu.pytop250.csv','w',encoding='gbk') as f:
    for a in range(10):
        url = 'https://book.douban.com/top250?start={}'.format(a*25)
        data = requests.get(url).text

        s=etree.HTML(data)
        file=s.xpath('//*[@id="content"]/div/div[1]/div/table')
        time.sleep(3)

        for div in file:
            title = div.xpath("./tr/td[2]/div[1]/a/@title")[0]
            href = div.xpath("./tr/td[2]/div[1]/a/@href")[0]
            score=div.xpath("./tr/td[2]/div[2]/span[2]/text()")[0]
            num=div.xpath("./tr/td[2]/div[2]/span[3]/text()")[0].strip("(").strip().strip(")").strip()
            scrible=div.xpath("./tr/td[2]/p[2]/span/text()")

            if len(scrible) > 0:
                f.write("{},{},{},{},{}\n".format(title,href,score,num,scrible[0]))
            else:
                f.write("{},{},{},{}\n".format(title,href,score,num))
