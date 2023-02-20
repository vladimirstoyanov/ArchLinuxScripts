sudo pacman --noconfirm -S  tor
sudo pacman --noconfirm -S torbrowser-launcher
sudo pacman --noconfirm -S  nyx

sudo systemctl enable tor.service
sudo systemctl start tor.service

torbrowser-launcher
