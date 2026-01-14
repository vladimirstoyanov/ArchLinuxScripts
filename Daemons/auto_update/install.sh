#!/bin/sh
echo "===Compiling auto update daemon..."
gcc -o auto_update auto_update.c

echo "===Coping auto_update binary and update_without_restart.sh script"
sudo cp auto_update /usr/bin/
sudo cp ../../Pacman/update_without_restart.sh /usr/bin/

echo "Generating a systemd service file..."
cp AutoUpdate.service /usr/lib/systemd/system/
systemctl enable  AutoUpdate
#cd ../../Systemd/
#sudo python start_daemon_at_boot_time_with_root_privileges.py AutoUpdate /usr/bin/auto_update AutoUpdate
