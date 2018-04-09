# wget -r "http://www.cangls.com/"
cd www.cangls.com/tag
for file in `ls *`
do 
	echo $file |sed 's/\.html//'
done

# bash get_pornstar_name.sh > pornstar_names.txt
# wc -l pornstar_names.txt
# Thanks to "http://www.cangls.com/". :)
