#Extracts one tar file.
#To extract all recursively, run this from bash console
#find data -name "*.tgz" | xargs -P 8 -I % bash extract_files.sh %

file=$1
dest=xmls/`dirname $file`
mkdir -p $dest
tar xzvf $file -C $dest

