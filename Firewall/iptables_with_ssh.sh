#!/bin/sh

# Clear all rules
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X

# Default policies
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow loopback
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Allow established and related connections
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# --- SSH ALLOW ---
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

# Drop invalid packets
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP

# Drop NULL packets
iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP

# SYN Flood protection (Limit)
iptables -N SYN_FLOOD
iptables -A SYN_FLOOD -m limit --limit 10/s --limit-burst 20 -j RETURN
iptables -A SYN_FLOOD -j DROP
iptables -A INPUT -p tcp --syn -j SYN_FLOOD

# Prevent XMAS packages
iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP

# Block ICMP (Ping)
iptables -A INPUT -p icmp -j DROP
iptables -A OUTPUT -p icmp -j DROP

#drop some custom ip addresses
sudo iptables  -I OUTPUT -d 217.10.240.0/22 -j DROP
sudo iptables  -I OUTPUT -d 88.203.128.0/24 -j DROP
sudo iptables  -I OUTPUT -d 87.227.139.160/27 -j DROP
sudo iptables  -I OUTPUT -d 87.227.139.144/28 -j DROP
sudo iptables  -I OUTPUT -d 87.227.139.140/30 -j DROP
sudo iptables  -I OUTPUT -d 216.105.32.0/20 -j DROP
sudo iptables  -I OUTPUT -d 87.230.98.64/28 -j DROP
sudo iptables  -I OUTPUT -d 216.105.32.0/20 -j DROP
sudo iptables  -I OUTPUT -d 82.118.229.0/24 -j DROP
sudo iptables  -I OUTPUT -d 149.248.0.0/18 -j DROP
sudo iptables  -I OUTPUT -d 37.19.203.0/24 -j DROP
sudo iptables  -I OUTPUT -d 85.91.143.128/26 -j DROP

iptables-save > /etc/iptables/iptables.rules
