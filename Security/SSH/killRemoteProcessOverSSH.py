import subprocess
import sys
import time

HOST="root@192.168.0.102"
PROCESS="mysqld"


def executeRemoteCommand (host, command):
    ssh = subprocess.Popen(["ssh", "%s" % host, command],
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
        return []
    else:
        #print result
        return result


cmdResult = executeRemoteCommand(HOST, "ps -A")

#get process ID
pid=""
for i in range(len(cmdResult)):
    splitResult = cmdResult[i].split(' ')
    splitResult= filter(None, splitResult) #igonre empy list members
    
    #0-pid
    #3-process
    #print splitResult
    if (len(splitResult)<4):
        continue
    
    splitResult[3]=splitResult[3].replace('\n','')
    if (PROCESS == splitResult[3]):
        pid = splitResult[0]

print "Process ID:" + pid

executeRemoteCommand(HOST, 'kill -9 ' + pid)
