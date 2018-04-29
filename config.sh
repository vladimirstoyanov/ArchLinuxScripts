echo "Enabling Network manager..."
sudo systemctl enable NetworkManager.service
sudo systemctl disable dhcpcd.service
sudo systemctl disable dhcpcd@.service
sudo systemctl stop dhcpcd.service
sudo systemctl stop dhcpcd@.service

echo "Enabling wireless..."
sudo systemctl enable wpa_supplicant.service
sudo systemctl start wpa_supplicant.service

#ToDo: resize plasma panel
echo "Resizing the Plasma panel..."

#ToDo: change default plasma theme
echo "Changing default plasma theme..."

#ToDo: change default wallpaper
echo "Changing default wallpaper..."

#ToDo: change default start menu icon
echo "Changing default start menu icon

echo "Configuring iptables..."
sh iptables.sh
systemctl enable iptables.service
systemctl reboot
