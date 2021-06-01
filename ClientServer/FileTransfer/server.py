#!/usr/bin/env python

import socket, threading
from random import randint
import hashlib
import os

private_key = 'password'
file_destination = ''

class ClientThread(threading.Thread):
    def __init__(self,ip,port, socket):
        threading.Thread.__init__(self)
        self.__ip = ip
        self.__port = port
        self.__socket = socket
        print "[+] New thread started for "+ip+":"+str(port)

    def ReturnHashOfFile(self, filepath, block_size=2**20):
		"""
		Return hash sum of file (filepath var)
		"""
		sha256 = hashlib.sha256()
		try:
		        f = open(filepath, 'rb')
		except IOError:
		        return ""
		while True:
			try:
			        data = f.read(block_size)
			except IOError:
			        f.close()
			        return ""
			if not data:
				break
			sha256.update(data)
		f.close()
		return sha256.hexdigest()


    def getHashAndFileName(self, data):
      """
      Return size, hash sum and name of file who will be received
      """
      file_size = ""
      file_hash = ""
      file_name = ""

      if len(data)==0:
	  return file_size,file_hash,file_name

      i=0;
      while(i<len(data) and data[i]!='#'):
	file_size+=data[i]
	i+=1
      i+=1

      while(i<len(data) and data[i]!='#'):
	file_hash+=data[i]
	i+=1
      i+=1

      for j in range(i,len(data),1):
	  file_name+=data[j]
      return file_size, file_hash, file_name


    def run(self):
        print "-------Connection from : "+ip+":"+str(port)

        self.__socket.send('')
	plain_text = self.__socket.recv(2048)

	if (plain_text != "hello"):
	  print "Error: data!=hello"
	  self.__socket.close()
	  return

	plain_text = 'get hash and file name'
	self.__socket.send(plain_text)
	plain_text = self.__socket.recv(2048)

	file_size, file_hash, file_name = self.getHashAndFileName(plain_text)

	try:
	  file_size = int(file_size)
	except:
	  print "Error: Cant convert file_size to int..."
	  self.__socket.close()
	  return

	if (len(file_hash) == 0 or len(file_name) == 0 or file_size < 1):
	    print "Error: if (len(file_hash) == 0 or len(file_name)==0 or file_size == 0):"
	    self.__socket.close()
	    return

	plain_text = 'get file'
	self.__socket.send(plain_text)

	##receiving encrypted file
	print "Receiving encrypted file..."
	f = open(file_destination + file_name, 'wb')
	data = self.__socket.recv(2048)
        while len(data)!=0:
	    f.write(data)
            data = self.__socket.recv(2048)
	f.close()

	if (os.path.isfile(file_destination+file_name) == False):
	  print "Error: Failed to receive file!"
	  self.__socket.close()
	  return


	print "Calculating checksum of " + file_destination + file_name
	file_hash2 = self.ReturnHashOfFile(file_destination + file_name)

	if (file_hash!=file_hash2):
	    print 'Error: Failed to receive file.'
	else:
	    print 'Done.'

	self.__socket.close()


host = "0.0.0.0"
port = 10128

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []


while True:
    tcpsock.listen(4)
    print "\nListening for incoming connections..."
    (clientsock, (ip, port)) = tcpsock.accept()
    clientsock.settimeout(5.0)
    newthread = ClientThread(ip, port, clientsock)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
