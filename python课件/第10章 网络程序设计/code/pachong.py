import sys
import multiprocessing
import re
import os

try:
    #Python 3
    import urllib.request as lib
    python3 = True
except Exception:
    #Python 2
    import urllib as lib
    python3 = False
def craw_links(url, depth, keywords, processed):
    '''url:the url to craw
       depth:the current depth to craw
       keywords:the tuple of keywords to focus
       pool:process pool
    '''
    contents = []
    if url.startswith('http://') or url.startswith('https://'):        
        if url not in processed:
            #mark this url as processed
            processed.append(url)
        else:
            #avoid processing the same url again
            return
        print('Crawing '+url+'...')
        fp = lib.urlopen(url)
        if python3:            
            #Python3 returns bytes, so need to decode. 
            contents = fp.read()
            contents_decoded = contents.decode('UTF-8')
        else:
            #Python2 returns str, does not need this decode
            contents_decoded = fp.read()
        fp.close()
        pattern = '|'.join(keywords)
        #if this page contains certain keywords, save it to a file
        flag = False
        if pattern:
            searched = re.search(pattern, contents_decoded)
        else:
            #if the keywords to filter is not given, save current page
            flag = True
        print(flag, searched)
        if flag or searched:
            if python3:
                with open('craw\\'+url.replace(':','_').replace('/','_'), 'wb') as fp:
                    fp.write(contents)
            else:
                with open('craw\\'+url.replace(':','_').replace('/','_'), 'w') as fp:
                    fp.write(contents_decoded)
        #find all the links in the current page
        links = re.findall('href="(.*?)"', contents_decoded)
        #craw all links in the current page
        for link in links:
            #consider the relative path
            if not link.startswith(('http://','https://')):                
                try:
                    index = url.rindex('/')
                    link = url[0:index+1]+link
                except:
                    pass
                
            if depth>0 and link.endswith(('.htm','.html')):
                craw_links(link, depth-1, keywords, processed)
                
if __name__=='__main__':   
    processed = []   
    keywords = ('KeyWord1','KeyWord2')
    if not os.path.exists('craw') or not os.path.isdir('craw'):
        os.mkdir('craw')
    craw_links(r'https://docs.python.org/3/library/index.html', 1, keywords, processed)
