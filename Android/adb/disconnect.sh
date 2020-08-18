#!/bin/sh
#$1 - IP address

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - IP address"
  exit 1
fi

abd disconnect $1:5555
