import re

import jieba
import numpy as np
import nltk

file_name = 'comment.csv'
def read_from_file(file_name):
    with open(file_name,'r') as fp:
       words = fp.read()
    return words
def stopwords(中文停用词表):
    words = read_from_file(中文停用词表)
    result = jieba.cut(words)
    new_words = []
    for r in result:
        new_words.append(r)
    return set(new_words)
def del_stop_words(words,stop_words_set):
    result = jieba.cut(words)
    new_words = []
    for r in result:
        if r in stop_words_set:
            new_words.append(r)
        return new_words