#!/bin/sh
#$1 - object file name

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - Object file name"
  exit 1
fi

objdump -D $1
