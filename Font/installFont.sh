#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - Font dir"
  exit 1
fi

sudo cp -r $1 /usr/share/fonts/
