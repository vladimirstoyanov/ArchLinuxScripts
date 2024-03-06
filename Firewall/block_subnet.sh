#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - network interface (e.g. eth0)"
        echo "1 arg - Subnet address"
  exit 1
fi


#sudo iptables -i $1 -A INPUT -s $2 -j DROP
sudo iptables  -A OUTPUT -s $2 -j DROP
#sudo iptables -i $1 -A FORWARD -s $2 -j DROP

iptables-save > /etc/iptables/iptables.rules
