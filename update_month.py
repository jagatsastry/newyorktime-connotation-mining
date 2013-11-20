import csv

for year in range(2007, 1986, -1):
    print "SELECT " + str(year) + ", curtime();"
    print """UPDATE words_""" + str(year) + """ w SET w.month = (SELECT m.month FROM month_article_map m WHERE w.article_id = m.article_id);"""

