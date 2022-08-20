#!/bin/sh
echo "===Compiling auto update daemon..."
gcc -o auto_update auto_update.c

echo "===Coping auto_update binary and update_without_restart.sh script" 
cp auto_update /usr/bin/
cp ../../Pacman/update_without_restart.sh /usr/bin/

echo "Generating a systemd service file..." 
cd ../../Systemd/
python start_daemon_at_boot_time_with_root_privileges.py AutoUpdate /usr/bin/auto_update AutoUpdate
 

