#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - package name"
  exit 1
fi

pacman -Qi $1 | grep "Depends on"
pacman -Qi $1 | grep "Required By"
