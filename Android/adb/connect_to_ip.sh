#!/bin/sh
#$1 - ip address

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - IP address"
  exit 1
fi


adb connect $1:5555
