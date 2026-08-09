#!/bin/sh

echo "Enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf"
echo "Uncomment these rows in /etc/pacman.conf"
echo "[multilib]"
echo "Include = /etc/pacman.d/mirrorlist"

#download the new database
pacman -Sy

pacman -Sl multilib
pacman -S steam
