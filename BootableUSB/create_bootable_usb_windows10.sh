#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - path to flash usb drive (/dev/sbx)"
        echo "2 arg - path to .iso file"
  exit 1
fi

woeusb --device $2 $1
