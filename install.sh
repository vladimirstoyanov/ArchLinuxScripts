#!/bin/bash
echo "Installing packman packages..."
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Installing: $line"
    pacman -S $line
done < "Package/pacman_packages"

echo "Installing pip packages..."
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Installing: $line"
    pip install $line
done < "Package/pip_packages"
