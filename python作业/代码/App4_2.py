#假设有一段英文，其中有单词中间的字母i误写为I，试修正
import re
s = "I am neither a bIg,nor a pig"
print(re.sub(r'(\w+)I(\w*)',r'\1i\2',s))


