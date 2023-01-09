#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - partition (e.g. /dev/sda)"
  exit 1
fi

sudo smartctl -t long $1
