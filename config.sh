#!/bin/sh
echo "Enabling Network manager..."
sudo systemctl enable NetworkManager.service
sudo systemctl disable dhcpcd.service
sudo systemctl disable dhcpcd@.service
sudo systemctl stop dhcpcd.service
sudo systemctl stop dhcpcd@.service
sleep 1

echo "Enabling wireless..."
sudo systemctl enable wpa_supplicant.service
sudo systemctl start wpa_supplicant.service
sleep 1

echo "Changing default plasma theme, wallpaper, etc."
python changeDefaultWallpaper.py
sudo cp ~/.config/plasma-org.kde.plasma.desktop-appletsrc ~/.config/plasma-org.kde.plasma.desktop-appletsrc_back
sudo cp ~/.config/plasmarc ~/.config/plasmarc_back 
sudo cp Resources/plasma-org.kde.plasma.desktop-appletsrc ~/.config/
sudo cp Resources/plasmarc  ~/.config/
sleep 1

#ToDo: change default start menu icon
#echo "Changing default start menu icon..."
#sudo cp Resources/logo250x250.svg /usr/share/icons/breeze-dark/apps/22/plasma.svg
#sudo cp Resources/logo250x250.svg /usr/share/icons/breeze-dark/preferences/32/plasma.svg
#sudo cp Resources/logo250x250.svg /usr/share/icons/breeze/apps/22/plasma.svg
#sudo cp Resources/logo250x250.svg /usr/share/icons/breeze/preferences/32/plasma.svg
#sleep 1

echo "Changing the keyboard layout and global shortcuts..."
sudo cp ~/.config/kglobalshortcutsrc ~/.config/kglobalshortcutsrc_back
sudo cp ~/.config/kxkbrc ~/.config/kxkbrc_back
sudo cp Resources/kglobalshortcutsrc ~/.config/
sudo cp Resources/kxkbrc ~/.config/
sleep 1

echo "Configuring iptables..."
sudo sh Firewall/iptables.sh
sudo systemctl enable iptables.service
sleep 1

echo "Adding printVulnearablePackages.sh on boot time..."
python2.7 ../Systemd/make_binary_to_start_on_boot_time.py printVulnearablePackages $(pwd)/BootTimeScripts/printVulnearablePackages.sh 'print vulnearable packages'
sleep 1

echo "Installing vulnearable packages plasma widget"
sh Plasma/install_widget.sh Plasma/PlasmaWidgets/Vulnerable_packages/
sleep 1

echo "Adding currentConnectedIpAddresses.sh on boot time..."
python2.7 ../Systemd/make_binary_to_start_on_boot_time.py current_connected_ip_addresses $(pwd)/BootTimeScripts/currentConnectedIpAddresses.sh 'list of connected ip addresses'
sleep 1

echo "Installing current connected ip addresses  plasma widget"
sh Plasma/install_widget.sh Plasma/PlasmaWidgets/Current_connected_ip_addresses/
sleep 1

echo "Adding getCurrencies.sh on boot time..."
python2.7 ../Systemd/make_binary_to_start_on_boot_time.py get_currencies $(pwd)/BootTimeScripts/getCurrencies.sh 'Currencies rates'
sleep 1

echo "Installing currencies plasma widget"
sh Plasma/install_widget.sh Plasma/PlasmaWidgets/curriences_rates/
sleep 1

sudo systemctl reboot
