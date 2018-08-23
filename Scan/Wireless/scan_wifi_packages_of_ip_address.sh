ifconfig $1 down #$1 - wifi interface
iw $1 set monitor control 
ifconfig $1 up
tcpdump -A -i $1 tcp and src $2 #$2 - scanned ip address
