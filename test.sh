#!/bin/bash
if [[ $(diff -b -q "sorted.txt" <(python sorter.py)) ]]; then
	echo incorrect forward result
	exit 1
else
	echo correct forward result
fi
if [[ $(diff -b -q "reversesorted.txt" <(python sorter.py -r)) ]]; then
	echo incorrect reverse result
	exit1
else
	echo correct reverse result
fi
exit 0
