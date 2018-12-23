#$1 - a newtwork interface with internet access
#$2 - a network interface that shares the internet

#installing dhcp server
echo "installing dhcp..."
echo y | pacman -S dhcp 

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - a newtwork interface with internet access"
        echo "2 arg - a network interface that shares the internet"
  exit 1
fi


echo "enabling ipv4 package forward..."
#enabling ipv4 package forward
sysctl net.ipv4.ip_forward=1

echo "enabling nat..."
#enable nat
iptables -t nat -A POSTROUTING -o $1 -j MASQUERADE
iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i $2 -o $1 -j ACCEPT

echo "accepting incomming connection to UDP port 67 (DHCP) and UDP/TCP port 53 (DNS requests)"
#accepting incomming connection to UDP port 67 (DHCP) and UDP/TCP port 53 (DNS requests)
iptables -I INPUT -p udp --dport 67 -i $2 -j ACCEPT
iptables -I INPUT -p udp --dport 53 -s 10.10.10.0/24 -j ACCEPT
iptables -I INPUT -p tcp --dport 53 -s 10.10.10.0/24 -j ACCEPT

echo "enabling dhcpd v4..."
#enabling dhcpd v4
systemctl enable dhcpd4.service

#setting up the network interface
echo "setting up the network interface..."
ip link set up dev $2
ip addr add 10.10.10.1/24 dev $2

#coping dhcpd.conf to /etc
echo "coping dhcpd.conf to /etc"
cp dhcpd.conf /etc/

#restarting dhcpd serivce
echo "restarting dhcpd service..."
systemctl stop dhcpd4.service
sleep 5
systemctl start dhcpd4.service
