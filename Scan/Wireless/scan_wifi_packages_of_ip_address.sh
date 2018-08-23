
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - wifi interface"
  echo "2 arg - ip address to scan"
	exit 1
fi

ifconfig $1 down #$1 - wifi interface
iw $1 set monitor control
ifconfig $1 up
tcpdump -A -i $1 tcp and src $2 #$2 - scanned ip address
