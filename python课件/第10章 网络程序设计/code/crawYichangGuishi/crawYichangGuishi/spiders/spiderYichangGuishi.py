import scrapy

class MySpider(scrapy.spiders.Spider):
    #爬虫的名字，每个爬虫必须有不同的名字
    name = 'spiderYichangGuishi'
    
    #要爬取的小说首页，第一篇
    start_urls = ['http://bbs.tianya.cn/post-16-1126849-1.shtml']

    #对每个要爬取的页面，会自动调用下面这个方法
    def parse(self, response):
        #用来存放当前页中的小说正文
        content = []
        for i in response.xpath('//div'):
            #作者蛇从革的天涯账号
            if i.xpath('@_hostid').extract()==['13357319']:
                for j in i.xpath('div//div'):
                    #提取文本
                    c = j.xpath('text()').extract()
                    #过滤干扰符号
                    g = lambda x:x.strip('\n\r\u3000').replace('<br>', '\n').replace('|', '')
                    c = '\n'.join(map(g, c)).strip()
                    content.append(c)
                
        with open('result.txt', 'a+', encoding='utf8') as fp:
            fp.writelines(content)

        #获取下一页网址并继续爬取
        url = response.url
        d = url[url.rindex('-')+1:url.rindex('.')]
        next_url = 'http://bbs.tianya.cn/post-16-1126849-{0}.shtml'.format(int(d)+1)

        try:
            yield scrapy.Request(url=next_url, callback=self.parse)
        except:
            pass
