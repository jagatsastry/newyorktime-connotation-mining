import csv
import time
import sys
from numpy import *
import munkres
import pylibmc
from multiprocessing import Pool
import multiprocessing

currentms = lambda: int(round(time.time() * 1000))

startTime = currentms()

mc = {} #pylibmc.Client(["127.0.0.1"])
USE_MC = False

def debug(msg, level=1):
    if level > 4:
        print msg
    pass

root = sys.argv[1]
print root

M = genfromtxt('graphs/graphs/' + root + '.graph', delimiter='\t')

entMap = {}
for x in csv.reader(open('graphs/entitymaps/' + root + '.entmap'), delimiter='\t'):
    entMap[int(x[0])] = x[1]

wordMap = {}
for x in csv.reader(open('graphs/wordmaps/' + root + '.wordmap'), delimiter='\t'):
    wordMap[int(x[0])] = x[1]

mp ={}
for [ent, word, weight] in M:
    if weight <= 1: 
        continue
    if ent not in mp:
        mp[ent] = []
    mp[ent] += [(word, weight)]

for ent in mp:
    mp[ent] = list(reversed(sorted(mp[ent], key=lambda x: x[1])))

from nltk.corpus import wordnet as wn
from munkres import Munkres

def similarity(wi1, wi2):
    val = None
    if wi1 < wi2:
        wi1, wi2 = wi2, wi1
    key = 'wsim_' + str(wi1) + '_' + str(wi2)
    if key in mc:
        return mc[key]
    
    try:
        word1 = wn.synset(".".join(wordMap[wi1].split('_') + ['01']))
        word2 = wn.synset(".".join(wordMap[wi2].split('_') + ['01']))
        val = word1.path_similarity(word2)
        debug(val, level=3)
        #print val
    except:
        pass
        #print("exc")

    if val == None:
        val = -2

    mc[key] = val

    return val

ents = [ (ent1, ent2) for ent1 in mp for ent2 in mp if (ent1 < ent2 and ( 2*abs(len(mp[ent1]) - len(mp[ent2])) < max(len(mp[ent1]), len(mp[ent2]))))]

from sets import Set

def handleEnt(ents):
        wordfileEntries = []
        outfileEntries = []
        m = Munkres()
        ent1, ent2 = ents
        t1 = currentms()        
#        print ent1,ent2
        w1 = list(array(mp[ent1])[:, 0])
        w2 = list(array(mp[ent2])[:, 0])
            
        """w1 = list(reversed(sorted(array(mp[ent1])[:, 0])))
        w2 = list(reversed(sorted(array(mp[ent2])[:, 0])))"""
       # w2 = [x[0] for x in reversed(sorted(mp[ent2], key=lambda x: x[1]))]
        
        w1 = w1[0:min(10, min(len(w1), len(w2)))]
        w2 = w2[0:len(w1)]
        #if(len(set(w1).intersection(set(w2))) == 0):
        #    return
        wSimMat = zeros((len(w1), len(w2)))
        #wSimMat = vectorize(lambda x,y: -1 * similarity(x, y)) (wSimMat)
        for i in range(len(wSimMat)):
            for j in range(len(wSimMat)):

                wSimMat[i][j] =  -1*similarity(w1[i], w2[j])
#        savetxt('wsim/mt_' + str(ent), array(wSimMat), delimiter="\t")
        t2 = currentms()

#        print "t2: ",t2 - t1
        indices = m.compute(copy(wSimMat))
        t3 = currentms()
        total = 0
        count = 0
#        print "t3: ",t3 - t2
        for row, column in indices:
            value = wSimMat[row][column]
            if value <= 0:
                total += -1 * value
                count += 1
                #wordfile.write("%s\t%s\t%2.3f\n" % (entMap[ent1], wordMap[w1[row]], -1 * value))
                #wordfile.write("%s\t%s\t%2.3f\n" % (entMap[ent2], wordMap[w2[column]], -1 * value))
                wordfileEntries.append("%4d\t%4d\t%4d\t%4d\t%2.3f\n" % (ent1, w1[row], ent2, w2[column], -1 * value))

        t4 = currentms()
        if count > 0:
            total = float(total)/count
#        print ent1,ent2," t: ",t4 - t1
        #outfile.write("%s\t%s\t%2.3f\n" % (entMap[ent1], entMap[ent2], total))
        outfileEntry = "%4d\t%4d\t%2.3f\n" % (ent1, ent2, total)
        return outfileEntry, wordfileEntries

p = Pool(8)
entries = p.map(handleEnt, ents)
p.close()
"""
entries = []
for ent in ents:
    entries.append(handleEnt(ent))
"""

from itertools import chain

outfileEntries = list(sorted([e[0] for e in entries]))
wordfileEntries = list(chain.from_iterable([e[1] for e in entries]))


outfile = open("wsim_10_words/" + root + ".graph", "w")
wordfile = open("wsim_10_words/" + root + ".wscore", "w")

#savetxt(outfile, outfileEntries, delimiter='\t')
#savetxt(wordfile, wordfileEntries, delimiter='\t')
for entry in outfileEntries:
    outfile.write(entry)
    outfile.flush()

for entry in wordfileEntries:
    wordfile.write(entry)
    wordfile.flush()

totalTime = (currentms() - startTime)/1000
print "Total time for ",root,":",totalTime

