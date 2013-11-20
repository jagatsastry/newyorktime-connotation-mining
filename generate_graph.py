import sys
import os

recs = [ rec.strip().split("\t") for rec in open(sys.argv[1]) ]

oldMonth = 1234
maxEnt = 1
maxWord = 1
entityMap = {}
wordMap = {}
fw = None
entMapFile = None
wordMapFile = None
if os.path.exists("graphs") == False:
  os.mkdir("graphs")
if os.path.exists("graphs/entitymaps") == False:
  os.mkdir("graphs/entitymaps")
if os.path.exists("graphs/wordmaps") == False:
  os.mkdir("graphs/wordmaps")

for rec in recs:
  (month, entity, word, count) = (rec[0], rec[1], rec[2], int(rec[3]))

  if oldMonth != month:
    filename = "graphs/" + month + ".graph" 
    if fw != None:
      fw.close()
    fw = open(filename, "w")

    entmap_fn = "graphs/entitymaps/" + month + ".entmap" 
    if entMapFile != None:
      entMapFile.close()
    entMapFile = open(entmap_fn, "w")

    wordmap_fn = "graphs/wordmaps/" + month + ".wordmap" 
    if wordMapFile != None:
      wordMapFile.close()
    wordMapFile = open(wordmap_fn, "w")

    maxEnt = 1
    maxWord = 1
    entityMap = {}
    wordMap = {}
  
  if entity not in entityMap:
    entityMap[entity] = maxEnt
    entMapFile.write(str(maxEnt) + "\t" + entity + "\n")
    maxEnt += 1
  
  if word not in wordMap:
    wordMap[word] = maxWord
    wordMapFile.write(str(maxWord) + "\t" + word + "\n")
    maxWord += 1

  fw.write(str(entityMap[entity]) + "\t" + str(wordMap[word]) + "\t" + str(count) + "\n")
  oldMonth = month
