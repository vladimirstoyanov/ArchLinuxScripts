#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg  - arg 1 - path to plasma widget"
  exit 1
fi
plasmapkg2 -i $1
