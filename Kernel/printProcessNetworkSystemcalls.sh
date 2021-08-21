#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - PID"
  exit 1
fi


strace -t -e trace=network,read,write -p $1
