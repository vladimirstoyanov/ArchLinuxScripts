#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - interface (e.g. can0)"
  exit 1
fi

ip link set $1 up type can bitrate 1000000 sample-point 0.875
