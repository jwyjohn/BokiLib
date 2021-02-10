#!/bin/bash  
export LANG=C.UTF-8
TMPDIR=./tmp

for i in `ls $TMPDIR`;  
do   
	echo Taring: $i ...;  
	tar -czvf "./tmp/$i.tar.gz" "./tmp/$i" && rm -rf "./tmp/$i" 
done   
