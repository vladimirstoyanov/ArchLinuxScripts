#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg  - ip address range (for example 192.168.0.0/24)"
  exit 1
fi

nmap $1
