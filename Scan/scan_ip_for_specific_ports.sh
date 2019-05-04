#!/bin/sh
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg  - port"
  echo "2 arg - ip address range (for example: 192.168.0.0/24) or ip address (for example: 192.168.0.1)"
  exit 1
fi

nmap -p $1 $2 #$1 is a port, $2 is an IP address
