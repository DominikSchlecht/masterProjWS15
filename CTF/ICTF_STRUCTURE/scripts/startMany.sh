#!/bin/bash

pkill python
rm logTmp/*.log

for i in `seq -w 1 1000`;
do
#	echo item: $i
	python2.7 executeThemAll.py >> logTmp/$i.log &
	sleep 1	#rennt
	#sleep 1 # macht probleme
done

sleep 5
pkill python


