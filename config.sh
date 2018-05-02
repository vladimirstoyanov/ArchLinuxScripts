echo "Enabling Network manager..."
sudo systemctl enable NetworkManager.service
sudo systemctl disable dhcpcd.service
sudo systemctl disable dhcpcd@.service
sudo systemctl stop dhcpcd.service
sudo systemctl stop dhcpcd@.service

echo "Enabling wireless..."
sudo systemctl enable wpa_supplicant.service
sudo systemctl start wpa_supplicant.service

#ToDo: replace the username with some variable
echo "Changing default plasma theme, wallpaper, etc."
cp /home/scitickart/.config/plasma-org.kde.plasma.desktop-appletsrc /home/scitickart/.config/plasma-org.kde.plasma.desktop-appletsrc_back
cp /home/scitickart/.config/plasmarc /home/scitickart/.config/plasmarc_back
cp Resources/plasma-org.kde.plasma.desktop-appletsrc /home/scitickart/.config/
cp Resources/plasmarc  /home/scitickart/.config/

#ToDo: change default start menu icon
echo "Changing default start menu icon..."
#cp Resources/logo250x250.svg /usr/share/icons/breeze-dark/apps/22/plasma.svg
#cp Resources/logo250x250.svg /usr/share/icons/breeze-dark/preferences/32/plasma.svg
#cp Resources/logo250x250.svg /usr/share/icons/breeze/apps/22/plasma.svg
#cp Resources/logo250x250.svg /usr/share/icons/breeze/preferences/32/plasma.svg

echo "Changing the keyboard layout and global shortcuts..."
cp /home/scitickart/.config/kglobalshortcutsrc /home/scitickart/.config/kglobalshortcutsrc_back
cp /home/scitickart/.config/kxkbrc /home/scitickart/.config/kxkbrc_back
cp Resources/kglobalshortcutsrc /home/scitickart/.config/
cp Resources/kxkbrc /home/scitickart/.config/

echo "Configuring iptables..."
sh iptables.sh
systemctl enable iptables.service
systemctl reboot
