#!/bin/sh
#$1 - A partition (for example: /dev/sda)
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - A partition (for example: /dev/sda)"
  exit 1
fi

mkfs.ext4 $1
