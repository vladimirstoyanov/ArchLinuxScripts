#!/bin/sh

echo "Installing KDE..."
sh KDE/installKDE.sh

echo "Installing packman packages..."
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Installing: $line"
    pacman --noconfirm -S $line
    sleep 1
done < "Package/pacman_packages"

#remove not used packages
echo "Removing packman packages..."
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Removing: $line"
    pacman --noconfirm -Rs $line
    sleep 1
done < "Package/not_used_packages"


echo "Installing pip packages..."
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Installing: $line"
    pip install $line
done < "Package/pip_packages"
