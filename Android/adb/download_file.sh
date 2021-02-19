#!/bin/sh
#$1 - ip address

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - Android device file location"
	echo "2 arg - PC download location"
  exit 1
fi

adb pull $1 $2
