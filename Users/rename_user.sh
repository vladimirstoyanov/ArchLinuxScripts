#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - old username"
        echo "2 arg - new username"
  exit 1
fi

usermod -l $2 $1
