import sys
import os
import glob

maxEnt = 1
maxWord = 1
entityMap = {}
wordMap = {}
countMap = {}
ewf = open("graphs/entitymaps/all.entmap", "w")
wwf = open("graphs/wordmaps/all.wordmap", "w")

for fl in glob.glob("graphs/outfiles/*"):
 print fl
 recs = [ rec.strip().split("\t") for rec in open(fl) ]
 for rec in recs:
  (month, entity, word, count) = (rec[0], rec[1], rec[2], int(rec[3]))
  
  if entity not in entityMap:
    entityMap[entity] = maxEnt
    ewf.write(str(maxEnt) + "\t" + entity + "\n")
    maxEnt += 1

  if word not in wordMap:
    wordMap[word] = maxWord
    wwf.write(str(maxWord) + "\t" + word + "\n")
    maxWord += 1

  entityCode = entityMap[entity]
  wordCode = wordMap[word]

  if entityCode not in countMap:
    countMap[entityCode] = {}

  if wordCode not in countMap[entityCode]:
    countMap[entityCode][wordCode] = 0

  countMap[entityCode][wordCode] += count

ewf.flush()
wwf.flush()
ewf.close()
wwf.close()

fw = open("graphs/graphs/all.graph", "w")
print "Done with aggregation"

for entity in sorted(countMap):
  for word in sorted(countMap[entity]):
    fw.write(str(entity) + "\t" + str(word) + "\t" + str(countMap[entity][word]) + "\n")

fw.flush()
fw.close()

