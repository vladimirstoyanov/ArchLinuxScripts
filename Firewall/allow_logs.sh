iptables -A INPUT -j LOG
iptables-save > /etc/iptables/iptables.rules
