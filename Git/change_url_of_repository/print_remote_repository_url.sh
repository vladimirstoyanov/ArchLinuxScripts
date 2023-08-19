#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - path to repository"
  exit 1
fi

cd $1
git remote -v
