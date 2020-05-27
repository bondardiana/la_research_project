import csv


"""
Finding the vectors of filtered tweets using glovo25
"""


myfile = open("filtered.csv", 'r', encoding="utf-8", errors='ignore')
res = []
for line in myfile:
    line = line.split(",")
    res.append(line)

res = res[0]
lst = []
for i in res:
    i = i.replace("\n", "")
    i = i.split(" ")
    lst += i

vectorfile = open("glovo25d.csv", 'r', encoding="utf-8", errors='ignore')
vectors = []
for line in vectorfile:
    line = line.split(" ")
    vectors.append(line)
 
words_vectrs = []

def word2vector(lst):
    words_vectrs = []
    for i in lst:
        for j in vectors:
            if i == j[0]:
                words_vectrs.append([i, j])
    with open("wordsvect.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        for i in words_vectrs:
            writer.writerow(i)       
    return words_vectrs


result_vect = word2vector(lst)
print(len(result_vect))
print(result_vect)