#!/bin/sh
#$1 - source code 

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 - Source code" 
  exit 1
fi

go build $1
