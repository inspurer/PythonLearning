# -*- coding: utf-8 -*-
#Python提供了thread和threading模块来支持多线程编程
#thread模块提供了多线程的底层支持模块，以低级原始的方式来处理和控制线程
#threading模块基于thread模块进行封装，将线程的操作对象化，在语言层面上提供了丰富的特性
#在Python3中不存在thread模块，该模块被改名为_thread

import threading
import time
import sys
class test(threading.Thread):

    def __init__(self,name,delay):
        threading.Thread.__init__(self)
        self.name=name
        self.delay=delay

    def run(self):
        print('{0} delay for {1}'.format(self.name,self.delay))
        time.sleep(self.delay)
        c = 0
        while True:
            print('This is thread {0} on line {1}'.format(self.name,c))
            c += 1
            if c == 5:
                print('End of thread {0}'.format(self.name))
                break

t1=test('Thread 1',1)
t2=test('Thread 2',1)

t1.start()
print('Wait t1 to end')
#join()方法阻塞当前上下文环境的线程，直到调用此方法的线程终止或者达到指定的timeout
t1.join()   #try to comment this line
t2.start()
print('End of main')




#thread模块不支持守护线程，主线程退出的时候，所有的子线程不论是否还在工作，都会被强制结束，
#而且没有任何警告和退出前的清理工作
#threading模块支持守护线程，可以通过setDaemon()函数来设定线程的daemon属性，
#当daemon属性设置为True的时候表明主线程的退出可以不用等待子线程完成，
#默认情况下，daemon标志位False，所有的非守护线程结束后主线程才会结束
import threading
import time
def myfunc(a,delay):
    print('I will calculate square of {0} after delay for {1}'.format(a,delay))
    time.sleep(delay)
    print('calculate begins...')
    result=a*a
    print(result)
    return(result)

t1=threading.Thread(target=myfunc,args=(2,5))
t2=threading.Thread(target=myfunc,args=(6,8))
print(t1.isDaemon())
print(t2.isDaemon())
t2.setDaemon(True)
t1.start()
t2.start()



#使用Queue为多线程分配任务
import os
import queue
import threading
import urllib.request

class DownloadThread(threading.Thread):
    def __init__(self,myQueue):
        threading.Thread.__init__(self)
        self._queue=myQueue
    def run(self):
        while True:
            url=self._queue.get()
            print(self.name+' begin download '+url+'...')
            self.download_file(url)
            self._queue.task_done()
            print(self.name+' download completed!!!')
    def download_file(self,url):
        urlhandler=urllib.request.urlopen(url)
        fname=os.path.basename(url)+'.html'
        with open(fname,'wb') as f:
            while True:
                chunk=urlhandler.read(1024)
                if not chunk:
                    break
                f.write(chunk)

if __name__ == '__main__':
    urls=['http://wiki.python.org/moin/webprogramming',
          'https://www.createspace.com/3611970',
          'http://www.513gp.org/258.html']
    myQueue=queue.Queue()
    for i in range(5):
        t = DownloadThread(myQueue)
        t.setDaemon(True)
        t.start()

    for url in urls:
        myQueue.put(url)

    myQueue.join()
