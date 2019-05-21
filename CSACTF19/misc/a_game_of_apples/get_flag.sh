#! /bin/bash

while :
do
	python -c 'print("\n9"*1000)' |nc 34.74.132.34 1338 |grep "CSACTF{.*"
done
