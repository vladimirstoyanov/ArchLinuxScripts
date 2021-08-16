#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 - path to directory"
	echo "arg2 - output filename"
  exit 1
fi

cd $1
find -type f -exec md5sum '{}' \; > $2
