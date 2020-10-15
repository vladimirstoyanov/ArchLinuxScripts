#!/bin/sh

#$1 - filename
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - filename"
  exit 1
fi

hexdump -C $1
