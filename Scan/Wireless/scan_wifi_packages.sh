ifconfig $1 down #$1- wifi interface
iw phy phy0 interface add $2 type monitor #$2 - a new virtual interface
iw dev $2 set freq $3 #$3 - frequency (for example: 2420)
ifconfig $2 up 

tcpdump -A -i $2 -s0 -vv -X
