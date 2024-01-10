#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - a kernel module (.ko file)"
  exit 1
fi

insmod $1
