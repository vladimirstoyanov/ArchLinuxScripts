#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - A process name"
  exit 1
fi


sudo trace-cmd record -e syscalls -F $1
