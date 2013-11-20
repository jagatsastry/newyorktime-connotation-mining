import csv
from numpy import *

posWords = {}
for [word, polarity] in csv.reader(open('mpqa.csv'), delimiter=','):
        if polarity =='p':
            posWords[word] = True
        elif polarity == 'n':
            posWords[word] = False

allWords = []

print "reading all wordmap"
for [idx, word] in csv.reader(open('graphs/wordmaps/all.wordmap'), delimiter='\t'):
   allWords.append(word)

print "reading all graph"
X = genfromtxt('graphs/graphs/all.graph', delimiter='\t')
posCt = 0.0
negCt = 0.0

print "reading entries"
for [ent, wordIdx, weight] in  X:
    wordIdx = int(wordIdx)
    word = allWords[wordIdx - 1]
    if (word in posWords):
        if posWords[word] == True:
            posCt += weight
        else:
            negCt += weight

print posCt,negCt
print "n1: " + str(float(posCt)/(posCt + negCt)) + " p1: " + str(float(negCt)/(posCt + negCt)) 
