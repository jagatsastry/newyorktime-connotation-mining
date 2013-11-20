import sys
import csv

efl = 'graphs/neighbor_vote/' + sys.argv[1] + '.iter_' + sys.argv[2] + '.ent'
X = [p for p in csv.reader(open(efl), delimiter='\t')]

print "% of positive words connected to entities and % of such entities"
bckt = [ int(float(p[6])/10) for p in X]
cts = [0] * 11
for b in bckt:
    cts[b] += 1

for i in range(10, -1, -1):
    if i < 10:
        cts[i] += cts[i + 1]
    print ">=%3d\t%2.2f" % (i*10,100*cts[i]/float(len(bckt)))

print ""

print "% of entities with positive connotation"
bckt = [ int(10*float(p[1])) for p in X]
cts = [0] * 11
for b in bckt:
    cts[b] += 1

for i in range(10, -1, -1):
    if i < 10:
        cts[i] += cts[i + 1]
    print ">=%3d\t%2.2f" % (i*10,100*cts[i]/float(len(bckt)))



