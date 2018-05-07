#假设有一段英文文本，其中有单词连续重复了2次，去重只保留一个
import re
s = "This is is a desk"
s = re.sub(r'(\b\w+) \1', r'\1', s)
print(s)
