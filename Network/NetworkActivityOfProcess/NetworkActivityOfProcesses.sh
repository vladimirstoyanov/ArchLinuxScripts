#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 - Refresh time"
  exit 1
fi

while true
do
	netstat -tunp
	netstat -tunp >> log.txt
	sleep $1
	clear
done
