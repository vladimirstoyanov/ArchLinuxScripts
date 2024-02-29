#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - network interface (e.g. wlan0)"
        echo "1 arg - IP range (192.168.100.0/24)"
  exit 1
fi

sudo iptables -i $1 -A INPUT -s $1 -j DROP
sudo iptables -i $1 -A OUTPUT -s $1 -j DROP
sudo iptables -i $1 -A FORWARD -s $1 -j DROP

iptables-save > /etc/iptables/iptables.rules
