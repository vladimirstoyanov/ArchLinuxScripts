#accept all input, output, forward packages
iptables --policy INPUT ACCEPT
iptables --policy OUTPUT ACCEPT
iptables --policy FORWARD ACCEPT

iptables -Z; # zero counters
iptables -F; # flush (delete) rules
iptables -X; # delete all extra chains

iptables-save
