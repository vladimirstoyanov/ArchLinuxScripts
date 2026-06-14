#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        efibootmgr
        echo "1 arg  - boot num (e.g. result of efibootmgr. The string is BootXXXX, where X is a number.)"
  exit 1
fi

efibootmgr -b $1 -B
