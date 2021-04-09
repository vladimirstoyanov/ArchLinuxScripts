pacman -S grub
grub-install --target=i386-pc /dev/sda
sh regenerate_grub.sh
