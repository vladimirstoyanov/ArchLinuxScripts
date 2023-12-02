#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - directory to monitor"
  exit 1
fi

sudo inotifywait -m $1
