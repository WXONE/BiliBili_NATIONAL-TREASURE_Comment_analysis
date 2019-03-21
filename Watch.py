import os
import random
import re

import jieba
import numpy as np
import pandas as pd
import pyecharts
from jieba import posseg as psg
import collections


with open('comment.csv','r')as f:
    comment = f.read()
comment_list = comment.split('\n')
print('>>>累计评论数：%s\n'%len(comment_list))

data = []
temp = ['','','','','','']
for comment in  comment_list:
    comment = comment.split(',')
    if len(comment) == 1:
        temp[4] = comment[0]
        comment = temp
        data.append(comment)
    elif len(comment)!=5:
        pass
    else:
        data.append(comment)
data1 = pd.DataFrame(data,columns=['序号','昵称','性别','时间','内容','点赞'])
string1 = ''.join(data1['内容'])
import os
import random
import re

import jieba
import numpy as np
# def read_from_file(file_name):
#     with open(file_name,'r') as fp:
#        words = fp.read()
#     return words
# word_list = []
# stop_words = read_from_file(stop_words1.txt)
word_list = []
stop_words = ['就是','这是','但是','虽然','觉得','还是','没有','(',')',]
words = psg.cut(string1)
for x in words:
    if x.flag == 'x' :
        pass
    elif len(x.word) == 1:
        pass
    elif x.word.encode('utf-8') in stop_words:
        pass
    else:
        word_list.append(x.word)
c = collections.Counter(word_list)

attr = []
value = []
for x in c.most_common(10):
    attr.append(x[0])
    value.append(x[1])
Bar = pyecharts.Bar("评论中出现频率最高的10个词", "统计时间：2019-03-21")
Bar.add("出现次数", attr, value,mark_point=['max'],is_legend_show = False)
Bar