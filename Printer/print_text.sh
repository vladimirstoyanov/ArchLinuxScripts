#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - some text to print"
  exit 1
fi

echo $1 > /dev/usb/lp0
