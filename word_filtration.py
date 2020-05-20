import textblob
import nltk
import nltk
#nltk.download('wordnet')
f= open ("to_write.csv", 'w')
#nltk.download('averaged_perceptron_tagger')
twits_likes = []
import re
import vocabulary
from textblob import TextBlob
from nltk.probability import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer


def selecting_tweets():
    myfile = open("kuk.csv", 'r', encoding="utf-8", errors='ignore')
    i = 0
    j = 0
    twits = []

    for line in myfile:
        i += 1
        line = line.split(",")
        try:
            if (len(line)) > 4 and len(line[4]) > 20 and line[-1] == 'en\n':
                text = line[4]
                if i > 100000:
                    break
                j += 1
                text = text.replace("\n", "").replace(";", "").replace('"', '').replace("'", " ").replace(":",
                                                                                                          "").replace(
                    "!", "").replace("?", "").replace(",", "").replace(".", "").replace("’", " ")
                text0 = re.sub(r'#\w*', '', text)
                text1 = re.sub(r'[^a-zA-Z ]', '', text0)
                text2 = re.sub(r'http\w*', '', text1)
                text2 = text2.lower()
                twits.append(text2)
                twits_likes.append((text2, line[11]))


        except Exception as e:
            print(e)
            print(line)
            print(i)
            break
    return twits


twits = selecting_tweets()

print(len(twits_likes))
print(len(twits))
def filtration(twits):
    words = []
    for ii, i in enumerate(twits):
        lst = nltk.word_tokenize(i)
        lst = nltk.pos_tag(lst)
        PRP = ['i', 'he', 'she', 'it', 'they', 'is', 'are', 'have', 'has', 'had', 'my', 'her', 'his', 'their', 'did',
               'done', 'don', 'dont', 'isn', 'isnt', 'hes', 'be', 'been', 'was', 'were', 'will', 'much', 'more']
        types = ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
        verbs = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
        nouns = ['NN', 'NNS', 'NNP', 'NNPS']
        adj = ['JJ', 'JJR', 'JJS']
        let = ""
        for word, pos in lst:
            if (pos in types):
                if len(word) > 2:
                    if word not in PRP:
                        if pos in verbs:
                            word = WordNetLemmatizer().lemmatize(word, 'v')
                        if pos in nouns:
                            word = WordNetLemmatizer().lemmatize(word, 'n')
                        if pos in adj:
                            word = WordNetLemmatizer().lemmatize(word, 'a')
                        words.append(word)
                        let += word + " "
        if  twits_likes[ii][1] and twits_likes[ii][1]!= "FALSE" and twits_likes[ii][1]!="0":
            #f.write(let[:-1] +","+ str(twits_likes[ii][1]) + '\n')
            print(0)
        print(9)
        f.write(let[:-1] + "," + str(twits_likes[ii][1]) + '\n')
    return words

#dict_a = {}
a= filtration(twits)
#aa = []

#for i in range (0, len(a)-2 ):
#    aa.append(a[i]+" "+ a[i+1]+" "+ a[i+2])

#for el in a:

#    if el not in dict_a:
#        dict_a[el]=0
#    dict_a[el]+=1
#print(sorted(list(dict_a), key= lambda x: x[1])[:30])

# print(twits)

