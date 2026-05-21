pacman -S --noconfirm wireshark-qt
sudo usermod -aG wireshark $USER
newgrp wireshark
sudo chown root:wireshark /usr/bin/dumpcap
sudo chmod 755 /usr/bin/dumpcap
sudo setcap cap_net_raw,cap_net_admin+eip /usr/bin/dumpcap
sudo chgrp wireshark /usr/bin/dumpcap

sudo systemctl restart systemd-networkd
sudo systemctl restart NetworkManager
