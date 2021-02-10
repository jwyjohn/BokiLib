#!/bin/bash

export LANG=C.UTF-8
#export DOUJIN_DIR=$PWD
TMPDIR=./tmp

touch sha_result.txt
echo > sha_result.txt
for i in `ls $TMPDIR/*.tar.gz`;  
do   
	#echo SHA256ing: $i ...;  
	echo `sha1sum $i` `wc -c $i|cut -f1 -d" "` >> sha_result.txt &
done   

