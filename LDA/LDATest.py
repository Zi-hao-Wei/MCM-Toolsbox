from sklearn.datasets import fetch_20newsgroups 
remove = ('header','footers','quotes')
newsgroups_train=fetch_20newsgroups(subset="train",remove=remove)
newsgroups_test=fetch_20newsgroups(subset="test",remove=remove)
news = [' ' .join(filter(str.isalpha, raw.lower().split())) for raw in newsgroups_train .data + newsgroups_test .data]
# print(len(news))

import lda 
from sklearn.feature_extraction.text import CountVectorizer 
n_topics=20
n_iter=500
cvectorizer=CountVectorizer(min_df=5,stop_words='english')
cvz=cvectorizer.fit_transform(news)
# print(cvz)

lda_model=lda.LDA(n_topics=n_topics,n_iter=n_iter)
X_topics=lda_model.fit(cvz)

# print(X_topics.components_)
# print(X_topics.components_.shape)


t=X_topics.components_.transpose()
# print(t.shape)

from sklearn.manifold import TSNE
# # pca initializtion usually leads to better results
tsne_model = TSNE(n_components =2, verbose =1, random_state =0, angle =.99, init='pca')
# # 20-D -> 2-D
tsne_lda = tsne_model .fit_transform(t)

# print(tsne_lda)
# print(tsne_lda.shape)

_lda_keys = []

print(t.shape)
for i in range(0,t.shape[0]):
    # print(t[i])
    # print(t[i].argmax())
    _lda_keys.append(t[i].argmax())
# # # # 并获得每个主题的顶级单词：


import matplotlib.pyplot as plt 

# for i in 

# plt.show()









import numpy as np
# # import bokeh.plotting as bp
# # from bokeh.plotting import save
# # from bokeh.models import HoverTool
# n_top_words = 5 # number of keywords we show
# # # 20 colors
colormap = np.array([
"#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c",
"#98df8a", "#d62728", "#ff9896", "#9467bd", "#c5b0d5",
"#8c564b", "#c49c94", "#e377c2", "#f7b6d2", "#7f7f7f",
"#c7c7c7", "#bcbd22", "#dbdb8d", "#17becf", "#9edae5"
])

# print(tsne_lda.shape)
# print(_lda_keys)

for i in range(0,t.shape[0]):
    plt.plot(tsne_lda[i][0],tsne_lda[i][1],c=colormap[_lda_keys[i]])
plt.show()


# # print(X_topics)





# topic_summaries = []
# topic_word = lda_model.topic_word_ # all topic words
# vocab = cvectorizer.get_feature_names()
# for i, topic_dist in enumerate(topic_word):
#     print(np.argsort(topic_dist))

#     topic_words = np .array(vocab)[np.argsort(topic_dist)][: -(n_top_words + 1): -1] # get!
    
#     topic_summaries .append(' ' .join(topic_words)) # append!

# print(topic_summaries)