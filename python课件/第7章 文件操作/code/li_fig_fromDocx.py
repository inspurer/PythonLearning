from docx import Document
import re

result = {'li':[], 'fig':[], 'tab':[], 'tuozhan':[]}
doc = Document(r'C:\Python可以这样学.docx')

for p in doc.paragraphs:
    t = p.text
    if re.match('例\d+-\d+ ', t):
        result['li'].append(t)
    elif re.match('图\d+-\d+ ', t):
        result['fig'].append(t)
    elif re.match('表\d+-\d+ ', t):
        result['tab'].append(t)
    elif t.startswith('拓展知识'):
        index = t.index('。')
        result['tuozhan'].append(t[:index+1])
for key in result.keys():
    print('='*30)
    for value in result[key]:
        print(value)
