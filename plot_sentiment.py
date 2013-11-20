import csv
import sys

from numpy import *
from matplotlib import *
from pylab import *
import pylab
from common_mpl_props import *


SMOOTHEN = True
print sys.argv
if len(sys.argv) > 4:
    SMOOTHEN = False
SMOOTHEN = True #Dont smoothen
title_1 = 'Sentiment of \'' + sys.argv[3] + '\' by month'
if SMOOTHEN:
    title_1 += ' (smoothened)'
title(title_1, {'fontsize':'22'})
xlabel('Month', {'fontsize':'22'})
ylabel('Sentiment', {'fontsize':'22'})
ylim(-1.0, 1.0)

idx = 0
revmap = {}
months = []
for year in range(1987, 2008):
    for month in range(1, 13):
        monthrep = str(year) + '_' + str(month).zfill(2)
        revmap[monthrep] = idx
        idx+=1
        months.append(monthrep)


def plotSent(dataFile, legendLabel, style, color, linewidth=4):
    data = array([ (row[0].strip().split(".iter")[0], float(row[1].strip())) for row in csv.reader(open(dataFile), delimiter='\t') ])

    n = len(data)
    sent = data[:, 1]
    #print sent[0:10]
    if SMOOTHEN:
        sent = [float(x) for x in sent]
        #smoothSum = add(add(sent,  sent[1:] + [0]),  [0] +  sent[:-1])
        #smoothDiv = [2] + ( [3] * (len(sent) - 2)) + [2]
        windowSize = max(3, int(0.05 * n)) #Rationale: There are 10 ticks shown on UI. Try to have not more than one heavy fluctuation per tick
        smoothSum = [0] * n
        smoothDiv = [0] * n
        print windowSize
        for i in range(n):
            for j in range(max(0, i - windowSize/2), min(n-1, i + windowSize/2) + 1):
                smoothSum[i] += sent[j]
                smoothDiv[i] += 1

        sent = divide(smoothSum, smoothDiv)
    #num_ticks = (len(data) + 1)/min(10, len(data) + 1)
    print legendLabel
    print zip(data[:, 0], ["%2.3f" % (s) for s in sent])
    num_ticks = min(10, len(data) + 1)
    xvals = [revmap[month] for month in data[:, 0]]
    minMonth = revmap[min(data[:, 0])]
    maxMonth = revmap[max(data[:, 0])]
    ticks = list(linspace(minMonth, maxMonth, num_ticks).astype('uint32'))
    if ticks[-1] != maxMonth:
        ticks.append(maxMonth)
    xticks(ticks, [months[val] for val in ticks], rotation=20)
    #print sent[0:10]
    pylab.plot(xvals, sent, style, color=color, linewidth=linewidth, label=legendLabel)
    #xticks(range(1, len(data) + 1)[::num_ticks], data[:, 0][::num_ticks], rotation=20)
    #pylab.plot(range(1, len(data) + 1), sent, style, color=color, linewidth=linewidth)

#savefig("sent_img/" + str(millis))
#close()

plotSent(sys.argv[1], "Using connotation lexicon", 'd-', color='b', linewidth=2)
plotSent(sys.argv[2], "Using sentiment lexicon", 'o-', color='g', linewidth=2)
legend()
show()
