#!/bin/bash
if [ $# -eq 0 ]; then
	echo "no curl provided"
	exit 1
fi
prompt=$1
var=$(curl -s -w "%{http_code}" -o response_body.txt $prompt)
http_code=${var}
if [ "$http_code" -eq 200 ]; then 
	cat response_body.txt
else
	echo " failed to retreive data, status code: $http_code"
fi	
