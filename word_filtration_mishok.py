from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist
from textblob import TextBlob
import vocabulary
import re
import textblob
import nltk
import csv
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')


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
                if i > 4000:
                    break
                j += 1
                text = text.replace("\n", "").replace(";", "").replace('"', '').replace("'", " ").replace(
                    ":", "").replace("!", "").replace("?", "").replace(",", "").replace(".", "").replace("’", " ")
                text1 = re.sub(r'[^a-zA-Z ]', '', text)
                text2 = re.sub(r'http\w*', '', text1)
                text2 = text2.lower()
                twits.append(text2)

        except Exception as e:
            print(e)
            print(line)
            print(i)
            break
    return twits


twits = selecting_tweets()


def filtration(twits):
    words = []
    for i in twits:
        lst = nltk.word_tokenize(i)
        lst = nltk.pos_tag(lst)
        PRP = ['i', 'he', 'she', 'it', 'they', 'is', 'are', 'have', 'has', 'had', 'my', 'her', 'his', 'their',
               'did', 'done', 'don', 'dont', 'isn', 'isnt', 'hes', 'be', 'been', 'was', 'were', 'will', 'much', 'more']
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
                        words.append(word)

    return words


print(type(twits))
word_set = set()


for i in range(len(twits)):
    r = twits[i].split(' ')
    for k in range(len(r)):
        word_set.add(r[k])
# world_set.remove('')

word_list = list(word_set)

with open("mishok.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(word_list)
    for i in range(len(twits)):
        r = twits[i].split(' ')
        count_word = [0] * len(word_list)
        for k in range(len(word_list)):
            count_word[k] = r.count(k)
        row = [i]+count_word
        writer.writerow(row)
