import os
import sys
import subprocess
import socket
from sets import Set
import time
from time import gmtime, strftime

from Parse import TcpPacket
from DB import connectionDB

class ConnectionData:
	def __init__(self):
		self.ip=""
		self.port =""
		self.process_name=""

def getNetstatCommandOutput():
		p = subprocess.Popen(['netstat', '-apnt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		return out.split('\n')

def checkNetstatRow(data):
	if (len(data)<7):
		return False
	if (data[5] == 'TIME_WAIT'):
		return False
	return True

def getDataByIp(ip_address):
	rows = getNetstatCommandOutput()

	connection_data = ConnectionData()
	list_ip=[]
	for i in range(len(rows)):
		if (i<2): #skip some shit rows
			continue
		data=rows[i].split(' ')
		data = filter(None, data) #remove empty strings

		if (checkNetstatRow(data) == False):
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

	return connection_data

def getConnectionDataList ():
	rows = getNetstatCommandOutput()

	list_ip=[]
	for i in range(len(rows)):
		if (i<2): #skip some shit rows
			continue
		data=rows[i].split(' ')
		data = filter(None, data) #remove empty strings

		if (checkNetstatRow(data) == False):
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

def getWhoisCommandOutput(ip_address):
	p = subprocess.Popen(['whois', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()

	return out.split('\n')

def getCountryCityOrgName (ip_address):
	rows = getWhoisCommandOutput(ip_address)

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
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)#ToDo: use GGP (socket.getprotobyname('ggp')) instead socket.IPPROTO_TCP
except socket.error , msg:
    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
ip_addresses = Set()
connectionDB_ = connectionDB.ConnectionDB("ipData.sqlite")

while(True):
	#ToDo: handle send packages as well
	packet = s.recvfrom(65565)
	tcpPacket = TcpPacket.ParseTCP(packet)
	connection_data = getDataByIp(tcpPacket.getSourceAddress())

	if (connection_data.ip==""):
		continue

	time_ = strftime("Time: %Y-%m-%d %H:%M:%S", gmtime())

	connectionDB_.insertNetworkPackageData(time_, connection_data.ip, connection_data.port, connection_data.process_name, tcpPacket.getData())
	if (connection_data.ip in ip_addresses):
		continue
	ip_addresses.add(connection_data.ip)
	netName, city, country = getCountryCityOrgName(connection_data.ip)

	print "========================="
	print time_
	print "Process: " + connection_data.process_name
	print "IP, port: " + connection_data.ip + ":" + connection_data.port
	print netName
	print city
	print country
	connectionDB_.insertIPInfo(connection_data.ip, netName, city, country)
