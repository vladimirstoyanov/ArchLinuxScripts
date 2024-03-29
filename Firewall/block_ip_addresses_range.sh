#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - IP range (192.168.100.0/24)"
  exit 1
fi

sudo iptables -I OUTPUT -d $1 -j DROP

iptables-save > /etc/iptables/iptables.rules
