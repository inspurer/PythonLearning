from random import randint
from PIL import Image

#根据原始24位色BMP图像文件，生成指定数量含有随机噪点的临时图像
def addNoise(fileName, num):
    #这里假设原始图像为BMP文件
    if not fileName.endswith('.bmp'):
        print('Must be bmp image')
        return
    #生成num个含有随机噪点的图像文件
    for i in range(num):
        #打开原始图像
        im = Image.open(fileName)
        #获取图像尺寸
        width, height = im.size
        #每个结果图像中含有的噪点数量可能会不一样
        n = randint(1, 20)
        for j in range(n):
            #随机位置
            w = randint(0, width-1)
            h = randint(0, height-1)
            #修改随机位置的像素值
            im.putpixel((w,h), (0,0,0))
        #保存结果图像
        im.save(fileName[:-4]+'_'+str(i+1)+'.bmp')

#根据多个含有随机噪点的图像，对应位置像素计算平均值，生成结果图像
def mergeOne(fileName, num):
    if not fileName.endswith('.bmp'):
        print('Must be bmp image')
        return
    #列表推导式，打开上面的函数生成的所有含有噪点的图像
    ims = [Image.open(fileName[:-4]+'_'+str(i+1)+'.bmp') for i in range(num)]
    #创建新图像
    im = Image.new('RGB', ims[0].size, (255,255,255))
    for w in range(im.size[0]):
        for h in range(im.size[1]):
            #生成器推导式，计算所有临时图像中对应位置上像素值的平均值
            r = sum((tempIm.getpixel((w,h))[0] for tempIm in ims)) // num
            g = sum((tempIm.getpixel((w,h))[1] for tempIm in ims)) // num
            b = sum((tempIm.getpixel((w,h))[2] for tempIm in ims)) // num
            #写入结果图像中对应位置
            im.putpixel((w,h), (r,g,b))
    #保存最终结果图像
    im.save(fileName[:-4]+'_result.bmp')

#对比合并后的图像和原始图像之间的相似度
def compare(fileName):
    im1 = Image.open(fileName)
    im2 = Image.open(fileName[:-4]+'_result.bmp')
    width, height = im1.size
    #图像中的像素总数量
    total = width * height
    #两个图像中对应位置像素值相似的次数
    right = 0
    #判断是否相似的阈值
    expectedRatio = 0.05
    for w in range(width):
        for h in range(height):
            #获取两个图像同一位置上的像素值
            c1 = im1.getpixel((w,h))
            c2 = im2.getpixel((w,h))
            #生成器推导式，判断两个像素值各分量之差的绝对值是否小于阈值
            similar = (abs(i-j)<255*expectedRatio for i,j in zip(c1,c2))
            #如果每个分量都小于阈值，相似像素个数加1
            if all(similar):
                right += 1
    return (total, right)

if __name__ == '__main__':
    #生成4个临时图像，然后进行融合，并对比融合后的图像与原始图像的相似度
    addNoise('test.bmp', 4)
    mergeOne('test.bmp', 4)
    result = compare('test.bmp')
    print('Total number of pixels:{0[0]},right number:{0[1]}'.format(result))
