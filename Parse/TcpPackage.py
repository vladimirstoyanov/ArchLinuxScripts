import socket, sys
from struct import *

class ParseTCP:
    def __init__(self, packet):
            #packet string from tuple
            packet = packet[0]

            #take first 20 characters for the ip header
            self.ip_header = packet[0:20]

            iph = unpack('!BBHHHBBH4s4s' , self.ip_header)

            self.version_ihl = iph[0]
            self.version = self.version_ihl >> 4
            self.ihl = self.version_ihl & 0xF

            self.iph_length = self.ihl * 4

            self.ttl = iph[5]
            self.protocol = iph[6]
            self.s_addr = socket.inet_ntoa(iph[8]);
            self.d_addr = socket.inet_ntoa(iph[9]);

            self.tcp_header = packet[self.iph_length:self.iph_length+20]

            tcph = unpack('!HHLLBBHHH' , self.tcp_header)

            self.source_port = tcph[0]
            self.dest_port = tcph[1]
            self.sequence = tcph[2]
            self.acknowledgement = tcph[3]
            self.doff_reserved = tcph[4]
            self.tcph_length = self.doff_reserved >> 4

            self.h_size = self.iph_length + self.tcph_length * 4
            self.data_size = len(packet) - self.h_size

            self.data = packet[self.h_size:]

    def getIpHeader(self):
        return str(self.ip_header)

    def getVersion(self):
        return str(self.version)

    def getIhl (self): #ToDo: write the full name of Ihl. Check what is getIhl
        return str(self.getIhl)

    def getTtl (self):
        return str(self.ttl)

    def getProtocol (self):
        return str(self.protocol)

    def getSourceAddress (self):
        return str(self.s_addr)

    def getDestinationAddress (self):
        return str(self.d_addr)

    def getSourcePort (self):
        return str(self.source_port)

    def getDestinationPort (self):
        return str(self.dest_port)

    def getSequenceNumber (self):
        return str(self.sequence)

    def getAcknowkedgement (self):
        return str(self.acknowledgement)

    def getTcpHeaderLength (self):
        return str(self.tcph_length)

    def getData(self):
        return str(self.data)
