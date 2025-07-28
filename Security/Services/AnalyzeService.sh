#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - service (e.g. AutoUpdate.service)"
  exit 1
fi

/usr/bin/systemd-analyze security  $1
