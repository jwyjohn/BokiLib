#!/bin/bash
export LANG=C.UTF-8
export BOKI_DIR=~/.boki_client
export BOKI_URL=http://192.168.1.43:5000
export CURLOPT_FAILONERROR=TRUE

mkdir -p $BOKI_DIR
touch $BOKI_DIR/index.list

# index.list: hash|filename|size

function bokinfo(){
	curl $BOKI_URL/i/$1
	grep $1 $BOKI_DIR/index.list
}

function bokiupl(){
	#curl -X POST -H "Content-Type: multipart/form-data" -F "file=@$1" $BOKI_URL/u
	if [ $(curl -X POST -H "Content-Type: multipart/form-data" -F "file=@$1" $BOKI_URL/u) -eq "404" ];then
		echo "Upload Failed."
	else
		echo `sha1sum $1 | cut -d' ' -f1`\|${1##*/}\|`wc -c $1 | cut -d' ' -f1`
		echo `sha1sum $1 | cut -d' ' -f1`\|${1##*/}\|`wc -c $1 | cut -d' ' -f1` >> $BOKI_DIR/index.list
}

function bokiquery(){
	grep $1 $BOKI_DIR/index.list
}

function bokidl(){
	curl $BOKI_URL/$1 -o $2
	if [ $(echo $?) -eq "0" ];then echo `sha1sum $2 | cut -d' \
	' -f1`\|${2##*/}\|`wc -c $2 | cut -d' ' -f1`;fi
	grep $1 $BOKI_DIR/index.list
}
