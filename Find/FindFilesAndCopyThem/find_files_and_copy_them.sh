#!/bin/sh

if [ $# -ne 3 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 - a directory to find there recursively"
	echo "arg2 - name of a file(s), a regular expression"
	echo "arg3 - destination directory"
  exit 1
fi

find $1 -name '$2' -exec cp {} $3  \;
