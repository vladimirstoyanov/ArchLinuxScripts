#!/bin/sh

#update the system
sudo pacman -Suy

#print vulnerable packages
echo "Vulnerable packages: "
sudo python ../Security/printVulnerablePackages.py
sleep 10

echo "The system will restart..."
sleep 5

#sudo shutdown -r now
