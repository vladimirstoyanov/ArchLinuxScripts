#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - path to repository"
        echo "2 arg - branch name"
  exit 1
fi

cd $1 
git checkout -b $2
