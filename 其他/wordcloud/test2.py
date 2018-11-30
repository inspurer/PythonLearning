import pickle  
from os import path
import time
import jieba
import numpy as np
from PIL import Image,ImageSequence
import matplotlib.pyplot as plt  
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib.font_manager import FontProperties  
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)  #title不能中文
text = ''
ipath =  'mks.jpg'
fin = open(r'共产党宣言.txt',encoding='utf-8').read()
 
wordlist_after_jieba = jieba.cut(fin, cut_all = True)
text = " ".join(wordlist_after_jieba)
backgroud_Image = plt.imread(ipath)  
print('加载图片成功！')  
'''''设置词云样式'''  
wc = WordCloud(  
    background_color='white',# 设置背景颜色,这是设置成和背景图形的背景一样为白色,然后词的颜色就和背景图形的主体颜色一样了
    mask=backgroud_Image,# 设置背景图片  
    font_path='C:\Windows\Fonts\STZHONGS.TTF',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字  
    max_words=2000, # 设置最大现实的字数  
    stopwords=STOPWORDS,# 设置停用词  
    max_font_size=150,# 设置字体最大值  
    random_state=30# 设置有多少种随机生成状态，即有多少种配色方案  
)

#过滤关键词
key_words = ["他们","我们","这种","已经","但是","这个","一个","会主","资产阶级","无产阶级","自己"]
for key in key_words:
    text = text.replace(key,"")
wc.generate_from_text(text)  
print('开始加载文本')

#graph = backgroud_Image
#设置字体颜色为随渐变色背景图形渐变
image = Image.open(ipath)
graph = np.array(image)
img_colors = ImageColorGenerator(graph)  
wc.recolor(color_func=img_colors)

# 显示词云图
plt.figure(1)
plt.title("马克思",fontproperties=font_set)
plt.imshow(wc)  
# 是否显示x轴、y轴下标  
plt.axis('off')  
plt.show()
#time.sleep(3)
plt.close()

# 显示词云图
plt.figure(2)
plt.imshow(wc)  
# 是否显示x轴、y轴下标  
plt.axis('off')  
plt.show()

# 获得模块所在的路径的  
d = path.dirname(__file__)  
wc.to_file(path.join(d, "result.jpg"))  
print('生成词云成功!')  
