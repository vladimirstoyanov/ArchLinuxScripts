#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - path to linux-firmware.pkg.tar.zst"
  exit 1
fi

pacman -U $1
