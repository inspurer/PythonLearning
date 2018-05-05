# -*- coding:utf-8 -*-
# Filename: BinaryTree.py
# --------------------
# Function description:
# Creation, traverse of binary tree, remove nodes
# --------------------
# Author: Dong Fuguo
# QQ: 306467355
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-11-15, Updated on 2015-12-17
# --------------------
class BinaryTree:
    def __init__(self, value):
        self.__left = None
        self.__right =  None
        self.__data = value
        
    def insertLeftChild(self, value):  #创建左子树
        if self.__left:
            print('__left child tree already exists.')
        else:
            self.__left = BinaryTree(value)
            return self.__left
        
    def insertRightChild(self, value): #创建右子树
        if self.__right:
            print('Right child tree already exists.')
        else:
            self.__right = BinaryTree(value)
            return self.__right
        
    def show(self):
        print(self.__data)

    def preOrder(self):                #前序遍历
        print(self.__data)             #输出根节点的值
        if self.__left:
            self.__left.preOrder()     #遍历左子树
        if self.__right:
            self.__right.preOrder()    #遍历右子树

    def postOrder(self):               #后序遍历
        if self.__left:
            self.__left.postOrder()
        if self.__right:
            self.__right.postOrder()
        print(self.__data)

    def inOrder(self):                 #中序遍历
        if self.__left:
            self.__left.inOrder()
        print(self.__data)
        if self.__right:
            self.__right.inOrder()

if __name__ == '__main__':
    print('Please use me as a module.')
