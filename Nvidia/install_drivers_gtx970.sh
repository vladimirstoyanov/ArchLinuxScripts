cd $1
git clone https://aur.archlinux.org/nvidia-580xx-utils.git

cd nvidia-580xx-utils
sudo pacman -S --needed base-devel debugedit
makepkg -si

