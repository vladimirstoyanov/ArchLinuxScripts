#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - local package name"
  exit 1
fi

pacman -U $1
