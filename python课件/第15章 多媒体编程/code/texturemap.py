from PIL import Image
from math import floor

def textureMap(srcTextureFile, dstSurfaceFile, dstWidth, dstHeight):
    srcTexture = Image.open(srcTextureFile)
    dstSurface = Image.new('RGBA', (dstWidth, dstHeight))
    srcWidth, srcHeight = srcTexture.size
    for w in range(dstWidth):
        for h in range(dstHeight):
            dstSurface.putpixel((w,h), srcTexture.getpixel((floor(w/dstWidth*srcWidth), floor(h/dstHeight*srcHeight))))
    dstSurface.save(dstSurfaceFile)
    srcTexture.close()

im = Image.new('RGBA', (200,100))
im.save(r'd:\new.jpg')
textureMap(r'd:\test.png', r'd:\new.jpg', 30, 150)
