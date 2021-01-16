#!/bin/sh

echo "Installing kde packages..."
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Installing: $line"
    pacman --noconfirm -S $line
    sleep 1
done < "Package/pacman_kde_packages"

echo 'Enabling sddm.service'
systemctl enable sddm.service
sleep 1
