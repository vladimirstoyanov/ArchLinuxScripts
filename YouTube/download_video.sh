#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - YouTube video link"
  exit 1
fi

pytube $1
