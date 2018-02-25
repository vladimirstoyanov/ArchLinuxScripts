import os
import sys
import subprocess
import time
from time import gmtime, strftime

def getConnectedIPAddresses ():
	p = subprocess.Popen(['netstat', '-ant'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()

	rows = out.split('\n')

	list_ip=[]
	for i in range(len(rows)):
		if (i<2): #skip some shit rows
			continue
		data=rows[i].split(' ')
		data = filter(None, data) #remove empy strings
		if (len(data)<5):
			continue
		ip = data[4].split(':')
		if (ip<2):
			continue
		list_ip.append(ip)

	return list_ip

def getCountryCityOrgName (ip_address):
	p = subprocess.Popen(['whois', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	
	rows = out.split('\n')
	
	netName=""
	city=""
	country=""
	for i in range (len(rows)):
		if (rows[i].find('NetName:')!=-1):
			netName = rows[i]
			continue
		if (rows[i].find('City:')!=-1):
			city = rows[i]
			continue
		if (rows[i].find('Country:')!=-1):
			country=rows[i]
			continue
	return netName, city, country


while(True):
	list_ip = getConnectedIPAddresses()
	for i in range (len(list_ip)):
		netName, city, country = getCountryCityOrgName(list_ip[i][0])
		
		print strftime("%Y-%m-%d %H:%M:%S", gmtime())+ ": "+  list_ip[i][0] + ":" + list_ip[i][1] + " " + netName + " " + city + " " + country
	time.sleep(1)



	
		
