#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - a python package"
  exit 1
fi

pip install $1
