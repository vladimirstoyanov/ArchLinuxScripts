#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 - a global variable (e.g. VARIBALE=SOMETHING)"
  exit 1
fi

pwd >> /etc/environment
