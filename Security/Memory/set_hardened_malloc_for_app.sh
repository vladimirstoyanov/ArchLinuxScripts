#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - full path to the app (e.g. /usr/bin/firefox)"
  exit 1
fi


LD_PRELOAD="/usr/lib/libhardened_malloc.so" $1
