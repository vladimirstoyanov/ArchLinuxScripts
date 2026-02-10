#!/bin/sh

#$1 - filename
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - directory"
  exit 1
fi

du -s -h $1
