#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - a filename"
  exit 1
fi

git checkout -- $1
