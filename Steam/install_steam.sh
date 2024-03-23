#enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf:
#/etc/pacman.conf
#[multilib]
#Include = /etc/pacman.d/mirrorlist"

pacman -Sl multilib

pacman -S steam
