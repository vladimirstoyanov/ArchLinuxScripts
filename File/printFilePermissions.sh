#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - package name"
  exit 1
fi

stat --format '%a' $1
