echo 'Installing xorg'
sleep 1
pacman -S xorg

echo 'Installing plasma'
pacman -S plasma
sleep 1

echo 'Installing plasma-wayland-session'
pacman -S plasma-wayland-session
sleep 1

echo 'Installing kde-applications'
pacman -S kde-applications
sleep 1

echo 'Installing sddm (display manager)'
pacman -S sddm
sleep 1

echo 'Installing network manager'
pacmna -S networkmanager
sleep 1

echo 'Enabling sddm.service'
systemctl enable sddm.service
systemctl enable NetworkManager.service
sleep 1

echo 'Done'
sleep 2

reboot

