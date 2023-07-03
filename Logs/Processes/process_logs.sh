#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - process name"
  exit 1
fi

sudo journalctl _COMM=$1 -n 100
