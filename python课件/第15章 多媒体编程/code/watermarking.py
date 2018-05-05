from os import remove
from os.path import isfile 
from random import sample, choice
from PIL import Image

def mergeWaterMark(originPic, watermarkPic, logTxt):
    #原始图片和水印文件必须为图片格式
    if ((not originPic.endswith(('.jpg', '.bmp', '.png'))) or
        (not watermarkPic.endswith(('.jpg', '.bmp', '.png')))):
        return 'Error format.'
    
    #打开原图和水印图片，并获取大小
    imOrigin = Image.open(originPic)
    originWidth, originHeight = imOrigin.size
    imWaterMark = Image.open(watermarkPic)
    watermarkWidth, watermarkHeight = imWaterMark.size

    #随机生成水印位置
    allPositions = [(w,h) for w in range(originWidth) for h in range(originHeight)]
    positions = sample(allPositions, watermarkWidth*watermarkHeight)

    fpLog = open(logTxt, 'w')
    #写入水印文件大小
    fpLog.write(str((watermarkWidth,watermarkHeight))+'\n')
    
    for w in range(watermarkWidth):
        for h in range(watermarkHeight):
            c = imWaterMark.getpixel((w,h))
            c = c[:3]
            #只写入不是白色的像素
            if c != (255,255,255):
                p = choice(positions)
                #写入像素值
                imOrigin.putpixel(p, c)
                #避免重复修改同一个像素
                positions.remove(p)
                #生成日志文件，用来提取水印
                fpLog.write(str(p+(w,h))+'\n')
    fpLog.close()
    #生成加入水印的新图片
    imOrigin.save(originPic[:-4]+'_new'+originPic[-4:])

def restoreWaterMark(mergedPic, logTxt, watermarkPic):
    #首先删除原来提取过的水印文件
    if isfile(watermarkPic):
        remove(watermarkPic)
    imMerged = Image.open(mergedPic)
    with open(logTxt) as fp:
        for line in fp:
            #读取每一行并还原为元组
            line = eval(line.strip())
            #第一行是水印图片尺寸，先创建水印文件
            if len(line)==2:
                imWaterMark = Image.new('RGB', line, (255,255,255))
            else:
                #提取水印像素并写入水印文件
                c = imMerged.getpixel((line[0],line[1]))
                c = c[:3]
                imWaterMark.putpixel((line[2],line[3]), c)
    #保存提取的水印
    imWaterMark.save(watermarkPic)
                
    
#添加水印
mergeWaterMark('origin.bmp', 'watermark.png', 'logg.txt')
#提取水印
restoreWaterMark('origin_new.bmp', 'logg.txt', 'restoredWaterMark.png')            
