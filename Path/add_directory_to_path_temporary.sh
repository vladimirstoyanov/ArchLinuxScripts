#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - a direcotry"
  exit 1
fi
export PATH=$1:$PATH
