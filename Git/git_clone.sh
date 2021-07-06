#!/bin/sh

if [ $# -ne 3 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - remote user name"
	echo "2 arg - remote ip"
	echo "3 arg - remote path of the project"
  exit 1
fi

git clone $1@$2:$3
