x=2007 
while [ $x -ge 1987 ] ; do 
    echo $x
#    for col in month entity word ; do
    for col in lemma pos_str ; do

        echo " $col"
        echo "CREATE INDEX words_"$x"_"$col"_idx ON words_$x($col)" | mysql -p'44Jz2T' jagat 
    done
    echo "CREATE INDEX words_"$x"_month_entity_lemma_idx ON words_$x(month, entity, lemma)" | mysql -p'44Jz2T' jagat 
    x=`echo "$x - 1" | bc` 
done
