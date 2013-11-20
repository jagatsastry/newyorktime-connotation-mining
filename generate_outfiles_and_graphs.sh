year=2007

echo "Generating outfiles and graphs"
mkdir /home/localdirs/SHARED/jagat/nyt/graphs/outfiles -p
while [ $year -ge 1987 ] ; do
    echo $year
    OUTFILE=/home/localdirs/SHARED/jagat/nyt/graphs/outfiles/$year
    QRY="select month, entity, concat(lemma,'_',pos_str), count(*) from words_$year where pos_str != 'adverb' group by month, entity, lemma order by month, entity, lemma"
    echo $QRY | mysql --skip-column-names -p'44Jz2T' jagat > $OUTFILE
    echo " Graphs"
    python generate_graph.py $OUTFILE
    year=`echo "$year - 1" | bc`
done
