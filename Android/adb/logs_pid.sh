#!/bin/sh
#$1 - ip address

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - Process ID (PID)"
  exit 1
fi


adb shell logcat --pid $1
