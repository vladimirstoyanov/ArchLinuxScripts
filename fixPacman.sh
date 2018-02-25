sudo rm -r /etc/pacman.d/gnupg
sudo pacman -Sy gnupg archlinux-keyring 
sudo pacman-key --init
sudo pacman-key --populate archlinux 
sudo pacman-key --refresh-keys 
sudo pacman -Sc

rm -R /var/lib/pacman/sync
pacman -Syu
