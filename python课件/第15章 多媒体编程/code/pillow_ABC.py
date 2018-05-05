from PIL import Image, ImageDraw, ImageFont

def redraw(f, v1, v2):
    start = int(600*v1)
    end = int(600*v2)
    
    im = Image.open(f)

    for w in range(start):
        for h in range(36, 61):
            im.putpixel((w,h), (255,0,0))

    for w in range(start, end):
        for h in range(36,61):
            im.putpixel((w,h), (0,255,0))

    for w in range(end, 600):
        for h in range(36,61):
            im.putpixel((w,h), (255,0,255))

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('simsun.ttc',18)
    
                        
    draw.text((start//2,38), 'A', (0,0,0), font=font)
    draw.text(((end-start)//2+start,38), 'B',(0,0,0), font=font)
    draw.text(((600-end)//2+end,38), 'C', (0,0,0),font=font)

    im.save(f)

redraw(r'biaotou1.png',0.1,0.9)
