#!/bin/sh
#$1 - ip address

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - a shell command"
  exit 1
fi

sudo adb shell $1
