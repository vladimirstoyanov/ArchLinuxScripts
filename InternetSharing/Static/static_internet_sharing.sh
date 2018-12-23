#!/bin/sh
#$1 - a network interface with internet access 
#$2 - a network interface that shares the internet
#$3 - an IP address of the network interface that shares the internet

if [ $# -ne 3 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - a newtwork interface with internet access (wlp3s0)"
        echo "2 arg - a network interface that shares the internet (enp0s25)"
	echo "3 arg - an IP address of the network interface that shares the internet (10.10.10.1)"
  exit 1
fi

echo "Setting up a static IP address of the network interface that shares the internet..."
ip link set up dev $2 
ip addr add $3/24 dev $2

echo "Enabling packet forwarding..."
sysctl net.ipv4.ip_forward=1

echo "Enabling NAT..."
iptables -t nat -A POSTROUTING -o $1 -j MASQUERADE
iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i $2 -o internet0 -j ACCEPT

#ToDo: get network address by ip address
#echo "Allowing UDP port 67 (DHCP) and UDP/TCP port 53 (DNS requests)..."
#iptables -I INPUT -p udp --dport 67 -i $2 -j ACCEPT
#iptables -I INPUT -p udp --dport 53 -s 192.168.123.0/24 -j ACCEPT
#iptables -I INPUT -p tcp --dport 53 -s 192.168.123.0/24 -j ACCEPT

echo "Don't forget to set up client ip addresses!"
 
