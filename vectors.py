import numpy as np
from numpy import dot
from numpy import vectorize
from numpy.linalg import norm
import matplotlib.pyplot as plt
import sklearn
from sklearn.manifold import TSNE
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import sentiwordnet as swn
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


#creating a dictionary with vectors
myfile = open("wordsvect.csv", 'r', encoding="utf-8", errors='ignore')
fl = []
for line in myfile:
    fl.append(line)
fl = fl[::2]
word_dict = {}
for i in fl:
    a = i.index(",")
    key_word = i[:a]
    str_vector = i[a+2:-2]
    l = str_vector.replace("[", '').replace("'", '').replace("]", '').rstrip("\\n").split(",")[1:]
    for i in range(len(l)):
        l[i] = float(l[i])
    word_dict[key_word] = l


#cosine similarity
def cosine_similarity(vec_1, vec_2):
    if norm(vec_1) > 0 and norm(vec_2) > 0:
        return dot(vec_1, vec_2) / (norm(vec_1) * norm(vec_2))
    else:
        return 0.0    


def vec(s):
    return word_dict[s]


#closest words
def closest(token_list, vec_to_check, n=10):
    return sorted(token_list,
                  key=lambda x: cosine_similarity(vec_to_check, vec(x)),
                  reverse=True)[:n]


print(spacy_closest(word_dict, word_dict["monday"], n=5))


words =  list(word_dict.keys())

#plot of all vectors
tsne = TSNE(n_components=2, random_state=0)
vectors = [word_dict[word] for word in words]
Y = tsne.fit_transform(vectors[:1000])
plt.scatter(Y[:, 0], Y[:, 1])
for label, x, y in zip(words, Y[:, 0], Y[:, 1]):
    plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords="offset points")
plt.show()    


#list of adjetives
adj_lst = []
for i in words:
    n = nltk.word_tokenize(i)
    n =  nltk.pos_tag(n)
    if n[0][1] == "JJ":
        adj_lst.append(i)



#plot of adjectives
tsne = TSNE(n_components=2, random_state=0)
vectors = [word_dict[word] for word in adj_lst]
Y = tsne.fit_transform(vectors[:1000])
plt.scatter(Y[:, 0], Y[:, 1])
for label, x, y in zip(adj_lst, Y[:, 0], Y[:, 1]):
    plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords="offset points")
plt.show()  



#count number of positive and negative adjectives
pos = 0
neg = 0
pos_neg_words = []
for i in adj_lst:
    emb =  sid.polarity_scores(i)
    pos += emb["pos"]
    neg += emb["neg"]
    if emb['neu'] != 1.0:
        pos_neg_words.append(i)

print(pos_neg_words)
print(pos)
print(neg)


#plot of positive and negative adjectives
tsne = TSNE(n_components=2, random_state=0)
vectors = [word_dict[word] for word in pos_neg_words]
Y = tsne.fit_transform(vectors[:1000])
plt.scatter(Y[:, 0], Y[:, 1])
for label, x, y in zip(pos_neg_words, Y[:, 0], Y[:, 1]):
    plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords="offset points")
plt.show()  