#!/bin/sh

echo "Removing not used packages..."
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Installing: $line"
    pacman --noconfirm -R $line
    sleep 1
done < "not_used_packages"
