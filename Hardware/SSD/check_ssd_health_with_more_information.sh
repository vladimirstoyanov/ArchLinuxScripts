#!/bin/sh

#for more information: https://media.kingston.com/support/downloads/MKP_306_SMART_attribute.pdf

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - partition (e.g. /dev/sda)"
  exit 1
fi

sudo smartctl -a $1
