#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - a kernel module"
  exit 1
fi

modprobe -r $1
