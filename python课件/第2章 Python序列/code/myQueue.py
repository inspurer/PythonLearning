# -*- coding:utf-8 -*-
# Filename: myQueue.py
# --------------------
# Function description:
# Queue of my own implementation
# --------------------
# Author: Dong Fuguo
# QQ: 306467355
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-11-13, Updated on 2015-12-13
# --------------------

class myQueue:
    def __init__(self, size = 10):
        self._content = []
        self._size = size
        self._current = 0

    def setSize(self, size):
        if size < self._current:
            #如果缩小队列，应删除后面的元素
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def put(self, v):
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current+1
        else:
            print('The queue is full')

    def get(self):
        if self._content:
            self._current = self._current-1
            return self._content.pop(0)
        else:
            print('The queue is empty')

    def show(self):
        if self._content:
            print(self._content)
        else:
            print('The queue is empty')
        
    def empty(self):
        self._content = []

    def isEmpty(self):
        if not self._content:
            return True
        else:
            return False

    def isFull(self):
        if self._current == self._size:
            return True
        else:
            return False

if __name__ == '__main__':
    print('Please use me as a module.')
