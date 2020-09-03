#!/bin/sh
#$1 - network interface
#$2 - new mac address

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 - Network interface (wlp3s0)"
	echo "arg2 - A new MAC address (9c:b7:33:44:55:66)"
  exit 1
fi

#make_binary_to_start_on_boot_time

sudo ip link set dev $1 down
sudo ip link set dev $1 address $2
sudo ip link set dev $1 up

