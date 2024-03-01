import sys
import os

ip_range = "18.32.0.0/11"
interface = 'wlp4s0'
rules = ['iptables -i ' + interface + ' -A INPUT -s ' + ip_range +' -j DROP',
        'iptables -A OUTPUT -s ' + ip_range +' -j DROP',
        'iptables -i ' + interface + ' -A FORWARD -s ' + ip_range + ' -j DROP']

for i in range (len(rules)):
        rules[i] = rules[i].replace(' -A ', ' -D ')
        os.system (rules[i])

#save changes

os.system ('iptables-save > /etc/iptables/iptables.rules')
