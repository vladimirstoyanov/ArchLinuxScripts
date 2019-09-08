#!/bin/sh
echo "Enabling Network manager..."
sudo systemctl enable NetworkManager.service
sudo systemctl disable dhcpcd.service
sudo systemctl disable dhcpcd@.service
sudo systemctl stop dhcpcd.service
sudo systemctl stop dhcpcd@.service

echo "Enabling wireless..."
sudo systemctl enable wpa_supplicant.service
sudo systemctl start wpa_supplicant.service

echo "Changing default plasma theme, wallpaper, etc."
python changeDefaultWallpaper.py
sudo cp ~/.config/plasma-org.kde.plasma.desktop-appletsrc ~/.config/plasma-org.kde.plasma.desktop-appletsrc_back
sudo cp ~/.config/plasmarc ~/.config/plasmarc_back 
sudo cp Resources/plasma-org.kde.plasma.desktop-appletsrc ~/.config/
sudo cp Resources/plasmarc  ~/.config/

#ToDo: change default start menu icon
echo "Changing default start menu icon..."
#sudo cp Resources/logo250x250.svg /usr/share/icons/breeze-dark/apps/22/plasma.svg
#sudo cp Resources/logo250x250.svg /usr/share/icons/breeze-dark/preferences/32/plasma.svg
#sudo cp Resources/logo250x250.svg /usr/share/icons/breeze/apps/22/plasma.svg
#sudo cp Resources/logo250x250.svg /usr/share/icons/breeze/preferences/32/plasma.svg

echo "Changing the keyboard layout and global shortcuts..."
sudo cp ~/.config/kglobalshortcutsrc ~/.config/kglobalshortcutsrc_back
sudo cp ~/.config/kxkbrc ~/.config/kxkbrc_back
sudo cp Resources/kglobalshortcutsrc ~/.config/
sudo cp Resources/kxkbrc ~/.config/

echo "Configuring iptables..."
sudo sh Firewall/iptables.sh
sudo systemctl enable iptables.service
sudo systemctl reboot

echo "Adding printVulnerablePackages.sh on boot time..."
cp BootTimeScripts/print_vulnerable_packages.target /usr/lib/systemd/system/
cp BootTimeScripts/printVulnerablePackages.sh /usr/local/bin/
