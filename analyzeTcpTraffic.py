import os
import sys
import subprocess
import socket
import time
from time import gmtime, strftime

from Parse import TcpPackage


class ConnectionData:
	def __init__(self):
		self.ip=""
		self.port =""
		self.process_name=""
def findIp(ip_address):
		p = subprocess.Popen(['netstat', '-apnt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()

		rows = out.split('\n')

		connection_data = ConnectionData()
		list_ip=[]
		for i in range(len(rows)):
			if (i<2): #skip some shit rows
				continue
			data=rows[i].split(' ')
			data = filter(None, data) #remove empy strings
			if (len(data)<7):
				continue
			#skip TIME_WAIT connectins
			if (data[5] == 'TIME_WAIT'):
				continue
			ip = data[4].split(':')
			if (ip<2):
				continue
			if (ip[0] != ip_address):
				continue

			connection_data = ConnectionData()
			connection_data.ip = ip[0]
			connection_data.port = ip[1]
			connection_data.process_name = data[6]
			return connection_data
			#list_ip.append(connection_data)
		return connection_data
		#return list_ip

def getConnectionData ():
	p = subprocess.Popen(['netstat', '-apnt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()

	rows = out.split('\n')

	list_ip=[]
	for i in range(len(rows)):
		if (i<2): #skip some shit rows
			continue
		data=rows[i].split(' ')
		data = filter(None, data) #remove empy strings
		if (len(data)<7):
			continue
		#skip TIME_WAIT connectins
		if (data[5] == 'TIME_WAIT'):
			continue
		ip = data[4].split(':')
		if (ip<2):
			continue
		connection_data = ConnectionData()
		connection_data.ip = ip[0]
		connection_data.port = ip[1]
		connection_data.process_name = data[6]
		list_ip.append(connection_data)

	return list_ip

def getCountryCityOrgName (ip_address):
	p = subprocess.Popen(['whois', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()

	rows = out.split('\n')

	netName=""
	city=""
	country=""
	for i in range (len(rows)):
		if (rows[i].find('NetName:')!=-1 or rows[i].find('netname')!=-1):
			netName = rows[i]
			continue
		if (rows[i].find('City:')!=-1 or rows[i].find('city:')!=-1):
			city = rows[i]
			continue
		if (rows[i].find('Country:')!=-1 or rows[i].find('country:')!=-1):
			country=rows[i]
			continue
	return netName, city, country

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error , msg:
    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

counter=0
while(True):
	#ToDo: create sqlite DB with IP addresses (send/recv packages, netName, city, country, whois information)
	packet = s.recvfrom(65565)
	counter+=1
	tcpPackage = TcpPackage.ParseTCP(packet)
	#print str(counter) + " : " + tcpPackage.getSourceAddress() + " : " + tcpPackage.getDestinationAddress()
	connection_data = findIp(tcpPackage.getSourceAddress())
	netName, city, country = getCountryCityOrgName(connection_data.ip)
	print "========================="
	print strftime("Time: %Y-%m-%d %H:%M:%S", gmtime())
	print "Process: " + connection_data.process_name
	print "IP, port: " + connection_data.ip + ":" + connection_data.port
	print netName
	print city
	print country
	"""
	list_ip = getConnectionData()
	for i in range (len(list_ip)):
		netName, city, country = getCountryCityOrgName(list_ip[i].ip)
		print "========================="
		print strftime("Time: %Y-%m-%d %H:%M:%S", gmtime())
		print "Process: " + list_ip[i].process_name
		print "IP, port: " + list_ip[i].ip + ":" + list_ip[i].port
		print netName
		print city
		print country
	time.sleep(1)
	"""
