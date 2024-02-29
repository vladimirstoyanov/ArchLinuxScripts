#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - IP range (192.168.100.0/24)"
  exit 1
fi
iptables -D OUTPUT -p all --destination $1


iptables-save > /etc/iptables/iptables.rules
