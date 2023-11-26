#!/bin/sh
sudo rm /var/lib/pacman/db.lck
sudo rm -r /etc/pacman.d/gnupg
sudo pacman -Sy --noconfirm gnupg archlinux-keyring
sudo pacman-key --init
sudo pacman-key --populate archlinux
sudo pacman-key --refresh-keys
sudo pacman -Sc --noconfirm

rm -R /var/lib/pacman/sync
sudo pacman -Syy --noconfirm archlinux-keyring
sudo pacman -Syyu --noconfirm
