#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - IP address"
  exit 1
fi

while true; do
    netstat -tunep | grep $1
    sleep 1
done
