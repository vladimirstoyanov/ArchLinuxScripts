#!/bin/sh

#update the system
pacman -Suy

#print vulnerable packages
#echo "Vulnerable packages: "
python ..Security/printVulnerablePackages.py
sleep 10

echo "The system will restart..."
sleep 1
#shutdown -r now
