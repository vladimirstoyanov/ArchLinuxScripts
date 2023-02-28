#!/bin/sh
if [ $# -ne 3 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - interface (e.g. can0)"
        echo "2 arg  - can ID (e.g. 201)"
        echo "3 arg  - can bytes (e.g. 00.FF.01)"
  exit 1
fi

cansend $1 $2\#$3
