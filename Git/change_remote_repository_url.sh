#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - remote URL"
	exit 1
fi

git remote set-url $1
