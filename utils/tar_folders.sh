#!/bin/bash  
export LANG=C.UTF-8
TMPDIR=../tmp

for i in `ls $TMPDIR`;  
do   
	echo Taring: $i ...;  
	#tar -czvf "TMPDIR/$i" "./$i.tar.gz"
done   
