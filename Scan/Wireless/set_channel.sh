#!/bin/sh
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - wifi interface"
  echo "2 arg - wifi channel"
  exit 1
fi

iw dev $1 set channel $2 #$1 - wifi interface, $2 - channel
