#!/bin/bash
if [ $# -eq 0 ]; then
	echo "No url found"
	exit 1
fi
var=$(curl -s  "$1" | wc -c)
echo "$var"
