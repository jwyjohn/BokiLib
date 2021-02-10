#!/bin/bash

export LANG=C.UTF-8
#export DOUJIN_DIR=$PWD
TMPDIR=./tmp

for i in `ls $TMPDIR/*.tar.gz`;  
do   
	echo "$i" $TMPDIR/`sha1sum $i|cut -f1 -d" "` 
done   

