import os
import sys
import time

path_to_service_files = '/usr/lib/systemd/system/'
def check_input ():
    if (len (sys.argv)!=3):
        print ("Wrong input:")
        print ("1 arg: network interface (wlp3s0)")
        print ("2 arg: mac addresss (9c:b7:FF:FF:FF:FF)")
        sys.exit()

def generate_service_file ():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    f = open ('chage_mac_' + sys.argv[1] + '.service', 'w')
    f.write('[Unit]\n')
    f.write('Description=MAC changer\n')
    f.write('After=network.target\n\n')
    f.write('[Service]\n')
    f.write('Type=simple\n')
    f.write ('ExecStart='+current_dir + 'change_mac_address_temporary.sh' +' '+ sys.argv[1] + ' ' + sys.argv[2] +'\n\n')
    f.write ('[Install]\n')
    f.write('WantedBy=multi-user.target\n')
    f.close()

def make_binary_to_start_on_boot_time ():
    os.system ('sudo mv chage_mac_' + sys.argv[1] + '.service ' + path_to_service_files)
    os.system('sudo systemctl enable chage_mac_' + sys.argv[1] + '.service')

check_input()
generate_service_file()
make_binary_to_start_on_boot_time()
