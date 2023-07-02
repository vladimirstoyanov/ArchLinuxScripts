#!/bin/sh

DNS=53
HTTP=80,443
IDENT=113
NTP=123
DHCP=67,68

#clear all rules
iptables -F

echo 'iptables -P INPUT DROP'
iptables -P INPUT DROP

echo 'iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT'
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

echo 'iptables -P FORWARD DROP'
iptables -P FORWARD DROP

echo 'iptables -P OUTPUT ACCEPT'
iptables -P OUTPUT ACCEPT

echo 'iptables -A INPUT -i lo -j ACCEPT'
iptables -A INPUT -i lo -j ACCEPT

#drop invalid packages
echo 'iptables -A INPUT -m conntrack --ctstate INVALID -j DROP'
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP

#drop NULL packets
echo 'iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP'
iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP

#prevent syn/syn-flood attacks
echo 'iptables -N SYN_FLOOD'
iptables -N SYN_FLOOD
echo 'iptables -A SYN_FLOOD -j DROP'
iptables -A INPUT -p tcp ! --syn -m conntrack --ctstate NEW -j DROP
iptables -A SYN_FLOOD -j DROP
echo 'iptables -A INPUT -p tcp --syn -j SYN_FLOOD'
iptables -A INPUT -p tcp --syn -j SYN_FLOOD

#prevent XMAS packages
echo 'iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP'
iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP

#drop icmp protocol
echo 'iptables -A OUTPUT -p icmp -j DROP'
iptables -A OUTPUT -p icmp -j DROP
echo 'iptables -A INPUT -p icmp -j DROP'
iptables -A INPUT -p icmp -j DROP

iptables-save > /etc/iptables/iptables.rules
