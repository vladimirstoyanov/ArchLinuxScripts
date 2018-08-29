#!/bin/sh
if [ $# -ne 3 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - wifi interface"
  echo "2 arg - a new virtual wifi interface"
  echo "3 arg - frequency of wifi (for example 2420)"
  exit 1
fi

ifconfig $1 down #$1- wifi interface
iw phy phy0 interface add $2 type monitor #$2 - a new virtual interface
iw dev $2 set freq $3 #$3 - frequency (for example: 2420)
ifconfig $2 up

tcpdump -A -i $2 -s0 -vv -X
