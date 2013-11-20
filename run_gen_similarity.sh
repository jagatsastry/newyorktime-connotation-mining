#months=`ls graphs/test_graphs/ | sed "s/.graph//g"`
echo "Running algorithm"
cat all_months | xargs -P 16 -I % python gen_similarity.py %
echo "DONE FOR 10"
#echo "100 now"
#cat all_months | xargs -P 2 -I % python gen_similarity_100.py %
#echo "DONE for 100"

