from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist
from textblob import TextBlob
import vocabulary
import re
import textblob
import nltk
import csv


'''In this file we deletenig unnecessary words from tweets and filter(tokenization, lemmatization, normalization)'''   

favs = []


def selecting_tweets():
    myfile = open("aaa.csv", 'r', encoding="utf-8", errors='ignore')
    i = 0
    j = 0
    twits = []
    for line in myfile:
        i += 1
        line = line.split(",")
        line[-1] = line[-1].replace(";", "")
        try:
            if (len(line)) > 4 and len(line[4]) > 20 and (line[-1] == 'en\n' or line[-1] == 'en"\n') and i != 3659:
                text = line[4]
                if i > 4000:
                    break
                j += 1
                text = text.replace("\n", "").replace(";", "").replace('"', '').replace("'", " ").replace(
                    ":", "").replace("!", "").replace("?", "").replace(",", "").replace(".", "").replace("’", " ")
                text1 = re.sub(r'[^a-zA-Z ]', '', text)
                text2 = re.sub(r'http\w*', '', text1)
                text2 = text2.lower()
                twits.append(text2)
                fav = line[11]
                try:
                    favs.append(int(fav))
                except:
                    favs.append(1)

        except Exception as e:
            print(e)
            print(line)
            print(i)
            print(int(line[11]))
            break
    return twits


twits = selecting_tweets()

def filtration(twits):
    res = []
    for i in twits:
        words = ''
        lst = nltk.word_tokenize(i)
        lst = nltk.pos_tag(lst)
        PRP = ['i', 'he', 'she', 'it', 'they', 'is', 'are', 'have', 'has', 'had', 'my', 'her', 'his', 'their',
               'did', 'done', 'don', 'dont', 'isn', 'isnt', 'hes', 'be', 'been', 'was', 'were', 'will', 'much', 'more', 'do', 'does','out']
        types = ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP',
                 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
        verbs = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
        nouns = ['NN', 'NNS', 'NNP', 'NNPS']
        adj = ['JJ', 'JJR', 'JJS']
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
                        words += word + " "
        res.append(words[:-1])
    with open("filtered.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(res)
    return res

#fil_twits = filtration(twits)


def mish_words(twits):
    word_set = set()
    for i in range(len(twits)):
        r = twits[i].split(' ')
        for k in range(len(r)):
            word_set.add(r[k])       
    word_list = list(word_set)
    res = ''
    res += str(word_list)
    res += "\n"
    with open("mishok.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(word_list)
    for i in range(len(twits)):
        r = twits[i].split(' ')
        count_word = [0] * len(word_list)
        for k in range(len(word_list)):
            count_word[k] = r.count(word_list[k])*favs[i]
        row = [i]+count_word
        res += str(row )
        res += '\n'
        writer.writerow(row)
    return res
