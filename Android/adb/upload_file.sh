#!/bin/sh
#$1 - file to upload
#$2 - target destination

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - file to upload"
        echo "2 arg - target destination"
  exit 1
fi


adb push $1 $2
