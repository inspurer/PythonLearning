from PIL import Image
import math

def qipan(width, height, color1, color2):
    im = Image.new('RGB',(width,height))
    for h in range(height):
        for w in range(width):
            if (math.floor(h/height*16)+math.floor(w/width*16)) % 2 == 0:
                im.putpixel((w,h), color1)
            else:
                im.putpixel((w,h), color2)
    im.save(r'd:\test.png')

if __name__=='__main__':
    qipan(500, 500, (255,0,0), (0,255,0))
