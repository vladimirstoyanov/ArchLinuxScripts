import sys
import os

def checkArguments ():
        if (len (sys.argv)!=3):
             print("Wrong input! please use the following input: ")
             print("    1 arg - network interface (e.g. wlp4s0)")
             print("    1 arg -ip range in CIDR format (e.g. 192.168.1.0/24)")
             sys.exit (0)

checkArguments()

ip_range = sys.argv[2]
interface = sys.argv[1]
rules = ['iptables -i ' + interface + ' -A INPUT -s ' + ip_range +' -j DROP',
        'iptables -A OUTPUT -s ' + ip_range +' -j DROP',
        'iptables -i ' + interface + ' -A FORWARD -s ' + ip_range + ' -j DROP']


for i in range (len(rules)):
        rules[i] = rules[i].replace(' -A ', ' -D ')
        os.system (rules[i])

#save changes
os.system ('iptables-save > /etc/iptables/iptables.rules')
