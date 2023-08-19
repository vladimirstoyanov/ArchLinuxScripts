#!/bin/sh

if [ $# -ne 3 ]
then
  echo "Wrong input! please use the following input: "
  echo "1 arg - origin"
	echo "2 arg - remote URL"
  echo "3 arg - path to the repository"
	exit 1
fi

cd $3
git remote set-url $1 $2
