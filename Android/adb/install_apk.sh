#!/bin/sh
#$1 - path to apk

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - path to apk"
  exit 1
fi

adb install $1
