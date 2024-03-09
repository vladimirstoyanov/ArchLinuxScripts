#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - iptables file with rules (e.g. /etc/iptables/iptables.rules)"
  exit 1
fi

sudo iptables -F  # flush all chains
sudo iptables -t nat -F  # flush nat chains (if applicable)
sudo iptables -X  # delete custom chains (if applicable)

sudo iptables-restore < $1
