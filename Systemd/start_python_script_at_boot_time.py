import os
import sys
import time

path_to_service_files = '/usr/lib/systemd/system/'
def check_input ():
    if (len (sys.argv)!=4):
        print ("Wrong input:")
        print ("1 arg: name")
        print ("2 arg: full path to the python script")
        print ("3 arg: description")
        sys.exit()

def generate_service_file ():
    f = open (sys.argv[1] + '.service', 'w')
    f.write('[Unit]\n')
    f.write('Description=' + sys.argv[3] + '\n')
    f.write('After=multi-user.target\n\n')
    f.write('[Service]\n')
    f.write('Type=idle\n')
    f.write ('ExecStart=/usr/bin/python '+sys.argv[2] + '\n\n')
    f.write ('[Install]\n')
    f.write('WantedBy=multi-user.target\n')
    f.close()

def make_binary_to_start_on_boot_time ():
    os.system ('mv ' + sys.argv[1] + '.service ' + path_to_service_files)
    os.system('systemctl enable ' + sys.argv[1])

check_input()
generate_service_file()
make_binary_to_start_on_boot_time()
