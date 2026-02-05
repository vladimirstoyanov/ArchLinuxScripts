#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - a torrent file"
  exit 1
fi

transmission-show $1
