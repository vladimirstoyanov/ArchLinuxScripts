#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - path to flash usb drive (e.g. /dev/sde, not /dev/sde1)"
        echo "2 arg - path to .iso file"
  exit 1
fi

wipefs --all --force $1
dd bs=4M if=$2 of=$1 status=progress oflag=sync
