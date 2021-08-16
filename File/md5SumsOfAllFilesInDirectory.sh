#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 - path to directory"
  exit 1
fi

cd $1
find -type f -exec md5sum '{}' \; > md5sum.txt
