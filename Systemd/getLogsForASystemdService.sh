#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - <service>.service"
  exit 1
fi

journalctl -rx --unit=$1
