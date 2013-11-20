entity=$1
keyword=$2
if [ "" = "$entity" -o "" = "$keyword" ] ; then
 echo "Usage: bash <filename> <entity> <keyword>"
 exit 1
fi

function dump_to_file() {
    dir_name=$1
    sent_dir="$dir_name"/sentiments
    if [ ! -e $sent_dir ] ; then
        mkdir $sent_dir
    fi

    NO_SMOOTH=$2
    file=$sent_dir/$keyword.sent
    if [ "$NO_SMOOTH" != "" ] ; then
        file="$file".sent
    else
        file="$file"_smooth.sent
    fi

    echo $file
    return
    grep "$entity" -i $dir_name/*iter_0*.ent   |  sed "s#$dir_name##g" | sed "s#^/##g" | sort -k 1 > $file
    echo $file
}

conn_dir="graphs/neighbor_vote_multiplier.conn/"
sent_dir="graphs/neighbor_vote_multiplier.sent/"

python plot_sentiment.py `dump_to_file $conn_dir $3` `dump_to_file $sent_dir $3` "$entity" $3
