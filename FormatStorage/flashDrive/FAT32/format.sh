#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - Flash drive label"
        echo "2 arg - path to usb device (/dev/sdb)"
  exit 1
fi

sudo mkfs.vfat -I -F 32 -n '$1' $2
