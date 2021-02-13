#!/bin/sh

if [ $# -ne 4 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - full path to video source"
        echo "2 arg - full path to video result"
        echo "3 arg - begin time (00:00:00 format)"
        echo "4 arg - duration (00:00:00 format)"
  exit 1
fi

ffmpeg -i $1 -ss $3 -t $4 -async 1 $2
