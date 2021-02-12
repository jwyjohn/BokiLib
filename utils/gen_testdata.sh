#!/bin/bash

export LANG=C.UTF-8
export DOUJIN_DIR=$PWD

#mkdir $DOUJIN_DIR/tmp/doujin{00001..99999}
for i in {00000..99999};
do
        mkdir -v "./tmp/doujin$i"
done

cd $DOUJIN_DIR/tmp

for doujin in `ls`;
do
	cd $DOUJIN_DIR/tmp/$doujin
	for i in {0..9};do dd if=/dev/urandom of=$i.img bs=1K count=1 iflag=fullblock;done
	pwd
	ls

done

#rm -rf $DOUJIN_DIR/tmp/*

exit 0
