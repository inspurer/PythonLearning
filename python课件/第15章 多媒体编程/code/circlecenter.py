from PIL import Image
import os

def searchLeft(width, height, im):
    for w in range(width): #从左向右扫描
        for h in range(height): #从下向上扫描
            color = im.getpixel((w, h)) #获取图像指定位置的像素颜色
            if color != (255, 255, 255):
                return w #遇到并返回椭圆边界最左端的x坐标


def searchRight(width, height, im):
    for w in range(width-1, -1, -1): #从右向左扫描
        for h in range(height):
            color = im.getpixel((w, h))
            if color != (255, 255, 255):
                return w #遇到并返回椭圆边界最右端的x坐标
            
def searchTop(width, height, im):
    for h in range(height-1, -1, -1):
        for w in range(width):
            color = im.getpixel((w,h))
            if color != (255, 255, 255):
                return h #遇到并返回椭圆边界最上端的y坐标

def searchBottom(width, height, im):
    for h in range(height):
        for w in range(width):
            color = im.getpixel((w,h))
            if color != (255, 255, 255):
                return h #遇到并返回椭圆边界最下端的y坐标

#遍历指定文件夹中所有bmp图像文件，假设图像为白色背景，椭圆为其他任意颜色
images = [f for f in os.listdir('testimages') if f.endswith('.bmp')]
for f in images:
    f = 'testimages\\'+f
    im = Image.open(f)
    width, height = im.size #获取图像大小
    x0 = searchLeft(width, height, im)
    x1 = searchRight(width, height, im)
    y0 = searchBottom(width, height, im)
    y1 = searchTop(width, height, im)
    center = ((x0+x1)/2, (y0+y1)/2)

    im.putpixel(center, (255,0,0)) #把椭圆中心像素画成红色
    im.save(f[0:-4]+'_center.bmp') #保存为新图像文件
    im.close()
