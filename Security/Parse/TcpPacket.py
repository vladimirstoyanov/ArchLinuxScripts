import socket, sys
from struct import *

class ParseTCP:
    def __init__(self, packet):
            #packet string from tuple
            packet = packet[0]

            #take first 20 characters for the ip header
            self.__ip_header = packet[0:20]

            iph = unpack('!BBHHHBBH4s4s' , self.__ip_header)

            self.__version_ihl = iph[0]
            self.__version = self.__version_ihl >> 4
            self.__ihl = self.__version_ihl & 0xF

            self.__iph_length = self.__ihl * 4

            self.__ttl = iph[5]
            self.__protocol  = iph[6]
            self.__s_addr = socket.inet_ntoa(iph[8]);
            self.__d_addr = socket.inet_ntoa(iph[9]);

            self.__tcp_header = packet[self.__iph_length:self.__iph_length+20]

            tcph = unpack('!HHLLBBHHH' , self.__tcp_header)

            self.__source_port = tcph[0]
            self.__dest_port = tcph[1]
            self.__sequence = tcph[2]
            self.__acknowledgement = tcph[3]
            self.__doff_reserved = tcph[4]
            self.__tcph_length = self.__doff_reserved >> 4

            self.__h_size= self.__iph_length + self.__tcph_length * 4
            self.__data_size = len(packet) - self.__h_size

            self.__data = packet[self.__h_size:]

    def getIpHeader(self):
        return str(self.__ip_header)

    def getVersion(self):
        return str(self.__version)

    def getIhl (self): #ToDo: write the full name of Ihl. Check what is getIhl
        return str(self.getIhl)

    def getTtl (self):
        return str(self.__ttl)

    def getProtocol (self):
        return str(self.__protocol )

    def getSourceAddress (self):
        return str(self.__s_addr)

    def getDestinationAddress (self):
        return str(self.__d_addr)

    def getSourcePort (self):
        return str(self.__source_port)

    def getDestinationPort (self):
        return str(self.__dest_port)

    def getSequenceNumber (self):
        return str(self.__sequence)

    def getAcknowkedgement (self):
        return str(self.__acknowledgement)

    def getTcpHeaderLength (self):
        return str(self.tcph_length)

    def getData(self):
        return str(self.__data)

    def getHexData(self):
        return str(self.__data).encode('hex')
