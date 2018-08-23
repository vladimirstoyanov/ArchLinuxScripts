if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg  - ip address range (for example: 192.168.0.0/24) or ip address (for example: 192.168.0.1)"
  exit 1
fi

sudo nmap -sS $1
