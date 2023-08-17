#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - a python version (e.g. 3.11)"
  exit 1
fi

sudo rm /usr/lib/python$1/EXTERNALLY-MANAGED
