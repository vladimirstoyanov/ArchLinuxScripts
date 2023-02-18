#!/bin/sh

if [ $# -ne 3 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - root partition (e.g. sda1)"
        echo "2 arg - home partition (e.g. sda2)"
        echo "3 arg - swap partition (e.g. sda3)"
        echo "Make sure that you have configured the parition table (e.g. with cfisk command)"
  exit 1
fi

echo "If you don't know the iso version, then cat version file in the root directory."

echo "=====Verifing signatures..."
gpg --keyserver-options auto-key-retrieve --verify archlinux-2023.02.01-x86_64.iso.sig
pacman-key -v archlinux-2023.02.01-x86_64.iso.sig

echo "=====Time: Setting NTP to true"
timedatectl set-ntp true

echo "=====Formating partitions..."
mkfs.ext4 /dev/$1
mkswap /dev/$3
mount /dev/$1 /mnt
swapon /dev/$3

echo "=====Installing basic packages, linux kernel, and linux-firmware...."
pacstrap /mnt base linux linux-firmware

echo "=====Formating the home partition..."
mkdir /mnt/home
mkfs.ext4 /dev/$2
mount /dev/$2 /mnt/home

echo "=====Generating fstab file with the partitions..."
genfstab -U /mnt >> /mnt/etc/fstab

echo "=====Trying to boot the installed arch..."
arch-chroot /mnt
