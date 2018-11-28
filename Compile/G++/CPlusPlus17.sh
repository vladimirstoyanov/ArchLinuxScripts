#!/bin/sh
#$1 - binary name
#$2 - source name

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - binary name"
        echo "2 arg - source file name" 
  exit 1
fi

g++ -std=c++1z -o $1 $2
