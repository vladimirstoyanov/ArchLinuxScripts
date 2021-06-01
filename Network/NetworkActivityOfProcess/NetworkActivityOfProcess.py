import os
import sys
import subprocess
import time

class CommandLineInput:
    def __init__ (self):
        pass

    def checkInput (self):
        if (len (sys.argv)!=3):
            print ("Wrong input:")
            print ("1 arg: process name")
            print ("2 arg: network interface name (wlp3s0)")
            sys.exit()

class ShellCommand:
    def __init__ (self):
        pass
    def getOutputOfCommand (self, command):
        result = ""
        try:
            result = subprocess.check_output(command, shell=True, text=True)
        except:
            pass
        return result

class ConnectedIPAddresses:
    def __init__ (self, processName):
        self.__processName = processName
        self.__shellCommand = ShellCommand ()

    def __getPIDByProcessName (self):
        commandOutput = self.__shellCommand.getOutputOfCommand ('ps -aux | grep ' + self.__processName)
        return self.__getListOfCommand(commandOutput, 1)

    def __getListOfCommand (self, commandOutput, index):
        result = []
        listRows = commandOutput.split('\n')

        for i in range (len(listRows)):
            listRow = listRows[i].split(' ')
            listRow = list(filter(None, listRow))
            if (len(listRow)<index+1):
                    continue
            result.append (listRow[index])
        return result

    def getConnectedIPAddresses (self):
        result = []
        processPIDs = self.__getPIDByProcessName ()
        for i in range (len(processPIDs)):
            commandOutput = self.__shellCommand.getOutputOfCommand('netstat -tnp | grep ' + processPIDs[i])
            ipAddresses = self.__getListOfCommand (commandOutput, 4)
            for j in range (len (ipAddresses)):
                result.append(ipAddresses[j])

        for i in range (len (result)):
            result[i] = result[i].split(':')
            result[i] = result[i][0]
        print (result)
        return result


class Wireshark:
    def __init__ (self, ipAddresses, networkInterface):
        self.__ipAddresses = ipAddresses
        self.__shellCommand = ShellCommand ()
        self.__networkInterface = networkInterface

    def __getFilter (self):
        filter = "("
        for i in range (len(self.__ipAddresses)):
            if (i==0):
                filter += "ip.dst==" + self.__ipAddresses[i]
            else:
                filter += " or ip.dst==" + self.__ipAddresses[i]
        filter +=')'
        return filter

    def open (self):
        if (len(self.__ipAddresses) == 0):
                print ("The process is not connected to any IP address.")
                return
        filter = self.__getFilter ()
        print ("Use this filter: " + filter)
        os.system ('sudo wireshark -i ' +self.__networkInterface + ' -k')

commandLineInput = CommandLineInput ()
commandLineInput.checkInput()
processName  = sys.argv[1]
interface = sys.argv[2]

connectedIPAddresses = ConnectedIPAddresses (processName)
ipAddresses = connectedIPAddresses.getConnectedIPAddresses()
wireshark = Wireshark (ipAddresses, interface)
wireshark.open()
