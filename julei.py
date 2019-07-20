from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from data_utils import *
import jieba
import matplotlib.pyplot as plt

# bigram 分词
segment_bigram = lambda text: " ".join([word + text[idx + 1] for idx, word in enumerate(text) if idx < len(text) - 1])
# jieba分词
segment_jieba = lambda text: " ".join(jieba.cut(text))
# 加载语料
corpus = []
with open("test.txt", "r", encoding="utf-8")as f:
    for line in f:
        # 去掉标点符号
        corpus.append(line.strip())
#计算tf-idf设为权重
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
"""
获取词袋模型中的所有词语特征
如果特征数量非常多的情况下可以按照权重降维
"""
word = vectorizer.get_feature_names()
print("word feature lenth:{}".format(len(word)))
#导出权重
tfidf_weight = tfidf.toarray()
# 指定成7个分类
kmeans = KMeans(n_clusters=7)
kmeans.fit(tfidf_weight)
#打印出每个簇的中心
print(kmeans.cluster_centers_)
for index,label in enumerate(kmeans.labels_,1):
    print("index:{},label:{}".format(index,label))
# 样本距其最近的聚类中心的平方距离之和，用来评判分类的准确度，值越小越好
# k-means的超参数n_clusters可以通过该值来评估
print("inertia: {}".format(kmeans.inertia_))
# 使用T-SNE算法对权重进行降维，准确度比PCA算法高，但是耗时长
tsne = TSNE(n_components = 2)
decomposition_data = tsne.fit_transform(tfidf_weight)
x = []
y = []
for i in decomposition_data:
    x.append(i[0])
    y.append(i[1])
fig = plt.fit_transform(figsize = (10,10))
ax = plt.axes()
plt.scatter(x,y,c = kmeans.labels_,marker = "x")
plt.xticks(())
plt.yticks(())
plt.savefig('/.sample.pbg',aspect = 1)