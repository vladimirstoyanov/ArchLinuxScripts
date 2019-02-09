#!/bin/sh
#$1 - path to binary
#$2 - path to coredump

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - path to binary"
        echo "2 arg - path to coredump"
  exit 1
fi

gdb $1 $2
