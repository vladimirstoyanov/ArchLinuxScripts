sudo pacman -S cups cups-pdf avahi nss-mdns

sudo systemctl enable --now cups.service
sudo systemctl enable --now avahi-daemon.service
