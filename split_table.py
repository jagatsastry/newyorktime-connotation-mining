import csv

arr = [(int(x[0]), str(x[1])) for x in csv.reader(open("ranges.csv"), delimiter="\t")]
idx = 0

for year in range(2007, 1986, -1):
    print "SELECT " + str(year) + ", curtime();"
    print "CREATE TABLE words_" + str(year) + " SELECT * FROM words WHERE article_id >= " + str(arr[idx][0]) + " AND article_id <= " + str(arr[idx][1]) + ";" 
    idx+=1

