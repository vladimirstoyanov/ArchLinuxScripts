#!/bin/sh
#$1 - binary
#$2 - a source file

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - binary name"
        echo "2 arg - source file name" 
  exit 1
fi

g++ -o $1 $2
