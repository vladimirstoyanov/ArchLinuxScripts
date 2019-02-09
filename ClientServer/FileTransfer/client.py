import sys
import socket
import hashlib
import os

private_key = 'password'

class Sender:
    def __init__(self,ip,port):
        self.ip = ip 
        self.port = port
    
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
    
    def getFileNameFromPath(self, path_to_file):
	"""
	From full path to file (path_to_file var), return only file name 
	"""
	separator = ''
	if (sys.platform.startswith('win')):
	    separator = '\\'
	else:
	    separator = '/'
	 
	file_name = ''
	for i in range(len(path_to_file)-1,-1,-1):
	  if (path_to_file[i] == separator):
	      return file_name
	  file_name = path_to_file[i] + file_name
	
	return ''
   
	
    def sendFile(self, path_to_file):
	"""
	Send file (path_to_file var) to 'self.ip' on port 'self.port'
	"""
        print "--------------------------"
        
        if (os.path.isfile(path_to_file) == 0):
	  print "Error: file \""+path_to_file+"\" not exist!"
	  return
	
	print "Calculating checksum of " + path_to_file
	hash_ = self.ReturnHashOfFile(path_to_file)
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(5.0)
	
	# Connect the socket to the port where the server is listening
	server_address = (self.ip, self.port)
	print >>sys.stderr, 'connecting to %s port %s' % server_address
	sock.connect(server_address)
	
	data = 'hello'
	sock.send(data)
	
	message = sock.recv(2048)
	
	if (message!='get hash and file name'):
	  print 'message!=get hash and file name'
	  sock.close()
	  return
	
	file_name = self.getFileNameFromPath(path_to_file)
	file_size = os.path.getsize(path_to_file)
	
	data = str(file_size) +'#'+hash_ + '#' + file_name
	sock.send(data)
	
	message = sock.recv(2048)
	if (message!='get file'):
	  print 'message!=get file'
	  sock.close()
	  return

	
	print "Sending file..."
	f = open (path_to_file, 'rb') 
	
	data = f.read(2032)
	while (data):
	  sock.send(data)
	  data = f.read(2032)
	
	f.close()
	sock.close()
	print "The file has been sent."


sender = Sender('127.0.0.1', 10128)
sender.sendFile('/home/scitickart/test.jpg')
