#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg  - arg 1 - a plasma widget name"
  exit 1
fi
plasmapkg2 -r $1
rm -rf ~/.local/share/plasma/plasmoids/$1
