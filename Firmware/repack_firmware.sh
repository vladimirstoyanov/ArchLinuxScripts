#!/bin/sh

#$1 - filename
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - firmware (.bin file)"
  exit 1
fi

binwalk -M -c $1
