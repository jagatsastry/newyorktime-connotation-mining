
for year in range(2007, 1986, -1):
    print "SELECT min(article_id), max(article_id) FROM month_article_map WHERE month LIKE \'" + str(year) + "_%\';"
