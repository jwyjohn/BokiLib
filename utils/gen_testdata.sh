#!/bin/bash

export LANG=C.UTF-8
export DOUJIN_DIR=$PWD

mkdir $DOUJIN_DIR/tmp/doujin{001..100}
cd $DOUJIN_DIR/tmp

for doujin in `ls`;
do
	cd $DOUJIN_DIR/tmp/$doujin
	for i in {0..9};do dd if=/dev/urandom of=$i.img bs=1M count=1 iflag=fullblock;done
	pwd
	ls

done

#rm -rf $DOUJIN_DIR/tmp/*

exit 0
