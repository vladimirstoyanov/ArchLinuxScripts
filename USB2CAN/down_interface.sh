#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - can interface (e.g. can0)"
  exit 1
fi

ip link set $1 down
