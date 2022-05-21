#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - hash of commit 1"
	echo "2 arg - hash of commit 2"
  exit 1
fi

git diff $1 $2
