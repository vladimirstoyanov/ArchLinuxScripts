#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - username"
  exit 1
fi

useradd -m $1
passwd $1
