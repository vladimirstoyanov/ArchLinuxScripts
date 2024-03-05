import os
import sys
import socket
import subprocess
import time
from time import gmtime, strftime

sys.path.insert(1, 'DB/')
import connectionDB

sys.path.insert(1, 'Parse/')
import TcpPacket

class ConnectionData:
	def __init__(self):
		self.__ip=""
		self.__port =""
		self.__process_name=""

	def setIp (self, ip):
		self.__ip = ip

	def setPort (self, port):
		self.__port = port

	def processName (self, process_name):
		self.__process_name = process_name

	def getIp (self):
		return self.__ip

	def getPort (self):
		return self.__port

	def getProcessName (self):
		return self.__process_name

	def setProcessName (self, process_name):
		self.__process_name =process_name

class Netstat:
	def __init__ (self):
			pass
	def __getNetstatCommandOutput(self):
			p = subprocess.Popen(['netstat', '-apntu'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			out, err = p.communicate()
			out = out.decode ('ascii')
			return out.split('\n')

	def __checkNetstatRow(self, data):
		sizeOfNetstatRow = 7
		indexOfState = 5
		if (len(data)<sizeOfNetstatRow):
			return False
		if (data[indexOfState] == 'TIME_WAIT'):
			return False
		return True

	def getDataByIp(self, ip_address):
		rows = self.__getNetstatCommandOutput()
		connection_data = ConnectionData()
		list_ip=[]

		for i in range(2,len(rows),1):
			data=rows[i].split(' ')
			data = list(filter(None, data))

			if (self.__checkNetstatRow(data) == False):
				continue

			ip = data[4].split(':')
			listSplitSize = 2
			ipIndex = 0
			portIndex = 1
			processIndex = 6
			if (len(ip)<listSplitSize):
				continue
			if (ip[ipIndex] != ip_address):
				continue

			connection_data = ConnectionData()
			connection_data.setIp(ip[ipIndex])
			connection_data.setPort(ip[portIndex])
			connection_data.setProcessName (data[processIndex])
			return connection_data

		return connection_data

class WhoIs:
	def __init__(self):
			pass

	def __getWhoisCommandOutput(self, ip_address):
		p = subprocess.Popen(['whois', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		out = out.decode ('ascii')
		return out.split('\n')

	def getCountryCityOrgName (self, ip_address):
		rows = self.__getWhoisCommandOutput(ip_address)

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



if __name__ == "__main__":
	try:
	    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)#ToDo: use GGP (socket.getprotobyname('ggp')) instead socket.IPPROTO_TCP
	except Exception as msg:
	    print ('Socket could not be created. Message: ' + str(msg))
	    sys.exit()

	ip_addresses = set()
	connectionDB_ = connectionDB.ConnectionDB("/root/ipData.sqlite")
	netstat = Netstat()
	whois = WhoIs()

	while(True):
		#ToDo: handle send packages as well
		packet = s.recvfrom(65565)
		tcpPacket = TcpPacket.ParseTCP(packet)
		connection_data = netstat.getDataByIp(tcpPacket.getSourceAddress())

		if ("" == connection_data.getIp()):
			continue

		time_ = strftime("Time: %Y-%m-%d %H:%M:%S", gmtime())

		connectionDB_.insertNetworkPackageData(
			time_,
			connection_data.getIp(),
			connection_data.getPort(),
			connection_data.getProcessName(),
			tcpPacket.getHexData()
		)
		if (connection_data.getIp() in ip_addresses):
			continue
		ip_addresses.add(connection_data.getIp())
		netName, city, country = whois.getCountryCityOrgName(connection_data.getIp())

		print ("=========================")
		print (time_)
		print ("Process: " + connection_data.getProcessName())
		print ("IP, port: " + connection_data.getIp() + ":" + connection_data.getPort())
		print (netName)
		print (city)
		print (country)
		connectionDB_.insertIpInfo(connection_data.getIp(), netName, city, country)
