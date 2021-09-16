#!/bin/sh

if [ $# -ne 3 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - root partition (e.g. /dev/sda1)"
        echo "2 arg - swap partition (e.g. /de/sda2)"
        echo "3 arg - username"
        echo "Make sure that you have configured the parition table (e.g. with cfisk command)"
  exit 1
fi

gpg --keyserver-options auto-key-retrieve --verify archlinux-version-x86_64.iso.sig
pacman-key -v archlinux-version-x86_64.iso.sig
timedatectl set-ntp true
mkfs.ext4 /dev/$1
mkswap /dev/$2
mount /dev/$1 /mnt
swapon /dev/$2
pacstrap /mnt base linux linux-firmware
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt
hwclock --systohc
locale-gen
echo "127.0.0.1	localhost\n">> /etc/hostname
echo "::1		localhost" >>/etc/hostname
mkinitcpio -P

echo "Enter root password"
passwd

cd /home
git clone https://github.com/vladimirstoyanov/ArchLinuxScripts.git
cd ArchLinuxScripts

echo "Creating a user $3"
sh ./Users/add_sudo_user.sh $3

sh install.sh
sh config.sh
exit
