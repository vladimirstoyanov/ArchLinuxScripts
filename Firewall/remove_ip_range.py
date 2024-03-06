import sys
import os

def checkArguments ():
        if (len (sys.argv)!=2):
             print("Wrong input! please use the following input: ")
             print("    1 arg -ip range in CIDR format (e.g. 192.168.1.0/24)")
             sys.exit (0)

checkArguments()

ip_range = sys.argv[1]
rules = ['iptables -A OUTPUT -d ' + ip_range +' -j DROP']


for i in range (len(rules)):
        rules[i] = rules[i].replace(' -A ', ' -D ')
        rules[i] = rules[i].replace(' -I ', ' -D ')
        print ("trying to remove a rule: " + rules[i])
        os.system (rules[i])

#save changes
os.system ('iptables-save > /etc/iptables/iptables.rules')
