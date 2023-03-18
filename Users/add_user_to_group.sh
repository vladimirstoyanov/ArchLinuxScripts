#!/bin/sh
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - username"
	echo "2 arg - group"
  exit 1
fi

sudo usermod -a -G $2 $1
