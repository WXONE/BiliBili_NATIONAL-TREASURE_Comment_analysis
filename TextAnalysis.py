import os
import random
import re

import jieba
import numpy as np
import nltk
#切词和去停用词
file_name = 'comment.csv'
def read_from_file(file_name):
    with open(file_name,'r') as fp:
       words = fp.read()
    return words
def stopwords(stop_words):
    words = read_from_file(stop_words)
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
    #构建词袋空间
def get_all_vector(file_path,stop_words_set):
    names = [os.path.join(file_path,f) for f in os.listdir(file_path)]
    posts = [open(name).read()for  name in names]
    docs = []
    word_set = set()
    for post in posts:
        doc = del_stop_words(post,stop_words_set)
        docs.append(doc)
        word_set |= set(doc)
    word_set = list(word_set)
    docs_vsm = []
    for doc in docs:
        temp_vector = []
        for word in word_set:
            temp_vector.append(doc.count(word) * 1.0)
        docs_vsm.append(temp_vector)

    docs_matrix = np.array(docs_vsm)
    #将单词出现的次数转化为TF-IDF权值
    column_sum = [float(len(np.nonzero(docs_matrix[:,i])[0])) for i in range(docs_matrix.shape[1])]
    column_sum = np.array(column_sum)
    column_sum = docs_matrix.shape[0]/column_sum
    idf = np.log(column_sum)
    idf = np.diag(idf)

    for doc_v in docs_matrix:
        if doc_v.sum() == 0:
            doc_v = doc_v/1
        else:
            doc_v = doc_v/(doc_v.sum())
        tfidf = np.dot(docs_matrix,idf)
    return names,tfidf
#用k-means算法聚类
def gen_sim(A,B):
    num = float(np.dot(A,B.T))
    denum = np.linalg.norm(A)*np.linalg.norm(B)
    if denum == 0:
        denum = 1
    cosn = num/denum
    sim = 0.5+0.5 * cosn
    return sim
def randCent(dataSet,k):
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = np.mat(minJ + rangeJ * random.rank(k,1))
    return centroids
def KMeans(dataSet,k,distMeas = gen_sim,createCent = randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroids = createCent(dataSet,k)
    clusterChanged = True
    counter = 0
    while counter <= 50:
        counter += 1
        clusterChanged = False
        for i in range(m):
            minDist = np.inf;
            minlndex = 1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI
                    minlndex = j
            if clusterAssment[i,0] != minlndex:
                clusterAssment = True
            clusterAssment[i,:] = minlndex,minDist**2
        for cent in range(k):
            ptslnClust = dataSet[np.nonzero(clusterAssment[:,0].A == cent)[0]]
            centroids[cent,:] = np.mean(ptslnClust,axis = 0)
    return centroids,clusterAssment