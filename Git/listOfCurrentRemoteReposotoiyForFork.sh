#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 - path to repository"
  exit 1
fi

cd $1 
git remote -v
