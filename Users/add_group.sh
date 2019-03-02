#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - group name"
  exit 1
fi

groupadd $1
