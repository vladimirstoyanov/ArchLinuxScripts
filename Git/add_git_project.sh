#!/bin/sh
#$1 - full path to the project

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - Full path to the project"
  exit 1
fi

mkdir -p $1
cd $1
git init --bare
