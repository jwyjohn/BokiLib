#!/bin/bash
export LANG=C.UTF-8
export BOKI_DIR=~/.boki_client
export BOKI_URL=http://192.168.1.43:5000

mkdir -p $BOKI_DIR
touch $BOKI_DIR/index.list

# index.list: hash|filename

function bokinfo(){
	curl $BOKI_URL/i/$1
}
