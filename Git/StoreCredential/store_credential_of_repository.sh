#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - path to git repository."
	      echo "2 arg - time (in seconds) you want Git to remember your credentials."
  exit 1
fi

cd $1
git config --global credential.helper store
git config credential.helper "cache --timeout $2"
