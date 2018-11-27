#!/bin/sh
#$1 - binary name
#$2 - source file

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - Binary name"
        echo "2 arg - Source file name"
  exit 1
fi

g++ -o $1 $2 -ggdb
