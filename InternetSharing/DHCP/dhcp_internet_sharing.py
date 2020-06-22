import os
import sys
import time

#$1 - a newtwork interface with internet access
#$2 - a network interface that shares the internet
#$3 - an IP address of the dhcp server

def generateDhcpdConfFile(dns1, dns2, gateway, network_address, first_three_numbers):
	f = open("dhcpd.conf", "w")
	f.write("option domain-name-servers " + dns1 +", " +dns2 +";\n")
	f.write("option subnet-mask 255.255.255.0; \n")
	f.write("option routers " + gateway + "; \n")
	f.write("subnet " + network_address + " netmask 255.255.255.0 { \n")
	f.write("\trange "+first_three_numbers+"150 "+first_three_numbers+"250; \n")
	f.write("}\n")
	f.write("\n")
	f.write("\n")
	f.write("\n")
	f.write("default-lease-time 600;\n")
	f.write("max-lease-time 7200;\n")
	f.close()

def help ():
	print ("1 arg - a newtwork interface with internet access (wlp3s0)")
	print ("2 arg - a network interface that shares the internet (enp0s25)")
	print ("3 arg - an IP address of dhcp server (10.10.10.1)")
	sys.exit(0)	

if (len(sys.argv)!=4):
	help()

#getting arguments
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

#getting the network address by server address
splitted_network_address = arg3.split('.')
if (len(splitted_network_address)!=4):
	print ("Invalid network address!")
	sys.exit (0)

network_address = splitted_network_address[0] + '.' + splitted_network_address[1] + '.' + splitted_network_address[2] + '.0'
gateway = splitted_network_address[0] + '.' + splitted_network_address[1] + '.' + splitted_network_address[2] + '.1'
first_three_numbers_of_ip = splitted_network_address[0] + '.' + splitted_network_address[1] + '.' + splitted_network_address[2] + '.'

#installing dhcp server
print ("installing dhcp...")
os.system("echo y | pacman -S dhcp")

print ("enabling ipv4 package forward...")
#enabling ipv4 package forward
os.system("sysctl net.ipv4.ip_forward=1")

print ("enabling nat...")
#enable nat
os.system("iptables -t nat -A POSTROUTING -o " + arg1 +" -j MASQUERADE")
os.system("iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT")
os.system("iptables -A FORWARD -i " + arg2 + " -o " + arg1 +" -j ACCEPT")

print ("accepting incomming connection to UDP port 67 (DHCP) and UDP/TCP port 53 (DNS requests)")
#accepting incomming connection to UDP port 67 (DHCP) and UDP/TCP port 53 (DNS requests)
os.system("iptables -I INPUT -p udp --dport 67 -i " + arg2 + " -j ACCEPT")
os.system("iptables -I INPUT -p udp --dport 53 -s "+network_address+"/24 -j ACCEPT")
os.system("iptables -I INPUT -p tcp --dport 53 -s "+network_address+"/24 -j ACCEPT")

print ("enabling dhcpd v4...")
#enabling dhcpd v4
os.system("systemctl enable dhcpd4.service")

#setting up the network interface
print ("setting up the network interface...")
os.system("ip link set up dev " + arg2)
os.system("ip addr add " + gateway + "/24 dev " + arg2) 

generateDhcpdConfFile('8.8.8.8', '8.8.4.4', gateway, network_address, first_three_numbers_of_ip) 

#coping dhcpd.conf to /etc
print ("coping dhcpd.conf to /etc")

os.system("mv dhcpd.conf /etc/")

#restarting dhcpd serivce
print ("restarting dhcpd service...")
os.system("systemctl stop dhcpd4.service")
time.sleep(5)
os.system("systemctl start dhcpd4.service")
