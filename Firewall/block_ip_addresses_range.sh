#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - IP start range"
        echo "1 arg - IP end range"
  exit 1
fi

iptables -A INPUT -m iprange –src-range [$1]-[$2] -j DROP
