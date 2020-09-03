import os
import sys
import time

#1 - interface
#2 - new mac address
path_to_service_files = '/usr/lib/systemd/system/'
path_link_files = '/etc/systemd/system/'

def check_input ():
    if (len (sys.argv)!=3):
        print ("Wrong input:")
        print ("1 arg: network interface (wlp3s0)")
        print ("2 arg: mac addresss (9c:b7:FF:FF:FF:FF)")
        sys.exit()

def generate_service_file ():
    f = open ('macspoof-' + sys.argv[1] + '.service', 'w')
    f.write('[Unit]\n')
    f.write ('Description=MAC Address Change ' + sys.argv[1] + '\n')
    f.write('Wants=network-pre.target\n')
    f.write('Before=network-pre.target\n')
    f.write('BindsTo=sys-subsystem-net-devices-' + sys.argv[1] + '.device\n')
    f.write('After=sys-subsystem-net-devices-' + sys.argv[1] + '.device\n')
    f.write('\n')
    f.write('[Service]\n')
    f.write('Type=oneshot\n')
    f.write('ExecStart=/usr/bin/ip link set dev ' + sys.argv[1] + ' address ' + sys.argv[2] + '\n')
    f.write('ExecStart=/usr/bin/ip link set dev ' + sys.argv[1] + ' up\n')
    f.write('\n')
    f.write('[Install]\n')
    f.write('WantedBy=multi-user.target\n')
    f.close()

def make_binary_to_start_on_boot_time ():
    os.system ('sudo mv macspoof-' + sys.argv[1] + '.service ' + path_to_service_files)
    #create a link
    os.system('sudo ln -s ' + path_to_service_files + 'macspoof-' + sys.argv[1] + '.service ' + path_link_files + 'macspoof-' + sys.argv[1] + '.service')

check_input()
generate_service_file()
make_binary_to_start_on_boot_time()
