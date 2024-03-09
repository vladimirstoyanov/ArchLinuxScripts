#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - Subnet address"
  exit 1
fi


#sudo iptables -i $1 -A INPUT -s $2 -j DROP
sudo iptables  -I OUTPUT -d $1 -j DROP
#sudo iptables -i $1 -A FORWARD -s $2 -j DROP

iptables-save > /etc/iptables/iptables.rules
