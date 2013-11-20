year=2007

echo "Creating tables"
while [ $year -ge 1987 ] ; do
    echo table"$year"
    echo "alter table word_aggregate_$year change column \`count(*)`` count int(11) " | mysql -p'44Jz2T' jagat
    for col in word lemma count ; do 
        echo $col
        echo "create index word_aggregate_""$year""_$col on word_aggregate_$year($col)" | mysql -p'44Jz2T' jagat
    done
    year=`echo "$year - 1" | bc`
done

