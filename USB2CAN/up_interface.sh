#!/bin/sh
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - can interface (e.g. can0)"
	      echo "2 arg  - bitrate (e.g. 500000)"
  exit 1
fi

ip link set $1 up type can bitrate $2 sample-point 0.875
