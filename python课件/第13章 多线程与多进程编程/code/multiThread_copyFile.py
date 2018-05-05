import os
import sys
import argparse
from queue import Queue
from threading import Thread
from shutil import copyfile

def copyFile(src, dst, num):
    '''使用num个线程复制src目录下的文件到dst目录中'''

    #源文件夹必须存在
    assert os.path.isdir(src), src+' must be an existing directory.'
    #如果目标文件夹不存在，创建一个
    if not os.path.isdir(dst):
        os.makedirs(dst)
    #最多容纳10个元素的队列
    q = Queue(10)
    
    def add(src):
        for f in os.listdir(src):
            f = os.path.join(src, f)
            if os.path.isfile(f):
                #往队列中放数据，满了会自动等待
                q.put(f)
            elif os.path.isdir(f):
                q.put(f)
                add(f)

    #创建并启动往队列中存放元素的线程
    t_add = Thread(target=add, args=(src,))
    t_add.start()

    def copy():
        while True:
            srcItem = q.get()
            if srcItem == None:
                break
            #替换字符串，生成目标路径
            dstItem = srcItem.replace(src, dst)
            print(srcItem, '==>', dstItem)
            if os.path.isfile(srcItem):
                dstDir = os.path.split(dstItem)[0]
                if not os.path.isdir(dstDir):
                    try:
                        os.makedirs(dstDir)
                    except FileExistsError as e:
                        pass
                copyfile(srcItem, dstItem)
            elif os.path.isdir(srcItem):
                try:
                    os.makedirs(dstItem)
                except FileExistsError as e:
                    pass
            #发送完成信号
            q.task_done()

    #创建指定数量的线程来复制文件
    for i in range(num):
        t = Thread(target=copy)
        t.start()

    #等待所有任务完成
    q.join()

    #往队列中插入None空值，让线程结束
    for i in range(num):
        q.put(None)

if __name__ == '__main__':

    #解析命令行参数
    parser = argparse.ArgumentParser(description='copy files from src to dst')
    parser.add_argument('-s', '--src')#, default='C:\\python35')
    parser.add_argument('-d', '--dst')#, default='D:\\test')
    parser.add_argument('-n', '--num', default='5')
    args = parser.parse_args()

    if args.src!=None and args.dst!=None:
        copyFile(args.src, args.dst, int(args.num))
    else:
        print('Please use the following command to see how to use:')
        print('  '+sys.argv[0]+' -h')
        
