import os
import sys

def checkInput ():
    if (len(sys.argv)!=2):
        print ("Wrong input! please use the following input: ")
        print ("1 arg - username")
        sys.exit (0)

checkInput ()
#os.system ('cp /etc/sudoers /ect/sudoers_org')#create backup
f = open ('/etc/sudoers', 'r')
f1 = open ('/etc/sudoers_new', 'w')
foundLine = False
for line in f.readlines ():
    if (line.find ('root ALL=(ALL:ALL) ALL')!=-1):
        foundLine = True
    elif (foundLine == True):
        foundLine = False
        f1.write (sys.argv[1] + " ALL=(ALL:ALL) ALL\n")

    f1.write (line)

f.close()
f1.close()
#replace file
os.system ('mv /etc/sudoers_new /etc/sudoers')
