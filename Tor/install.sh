sudo pacman -S tor
sudo pacman -S torbrowser-launcher
sudo pacman -S nyx

sudo systemctl enable tor.service
sudo systemctl start tor.service

torbrowser-launcher
