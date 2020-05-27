print("Top 30 words")
first_dict={}  # dict with number of total occuring of word
ff = open("filtered.csv", "r")
for line in ff:
    for word in line.split():
        if word not in first_dict:
            first_dict[word] = 0
        first_dict[word] += 1
ff.close()
from collections import  OrderedDict

dict1 = OrderedDict(sorted(first_dict.items() , key=lambda t: t[1]))
ff.close()
ff = open("filtered.csv", "r")
for el in list(dict1)[-30:-1]:
    line = "1" + ", " + str(el) + ", " + str(dict1[el])
    print(el, dict1[el], end=' , ')
print("\n")
print("Top 20 2-grams")
first_dict2={}  # dict with number of total occuring of word

for line in ff:
    line = line.split()
    for i in range(0, len(line)-1) :
        n_gram2 = line[i] +" "+ line[i+1]
        if n_gram2 not in first_dict2:
            first_dict2[n_gram2] = 0
        first_dict2[n_gram2] += 1
ff.close()
from collections import  OrderedDict
dict12 = OrderedDict(sorted(first_dict2.items() , key=lambda t: t[1]))

for el in list(dict12)[-20: -1]:
    print(el, dict12[el], end = " , ")
print("\n")

ff.close()
ff = open ("filtered.csv", "r")

print("Top 20 3-grams")

first_dict3={}  # dict with number of total occuring of word
for line in ff:
    line = line.split()
    for i in range(0, len(line)- 2 ) :
        n_gram3 = line[i] + " " + line[i+1]  +" " + line[i+2]
        if n_gram3 not in first_dict3:
            first_dict3[n_gram3] = 0
        first_dict3[n_gram3] += 1
ff.close()
from collections import  OrderedDict

dict13 = OrderedDict(sorted(first_dict3.items() , key=lambda t: t[1]))

for el in list(dict13)[-20: -1]:
    print(el, dict13[el], end = " , ")
