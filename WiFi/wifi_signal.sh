#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - interface (e.g. wlp4s0)"
  exit 1
fi

wavemon -i $1
