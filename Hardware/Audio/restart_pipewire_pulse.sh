systemctl --user restart wireplumber pipewire pipewire-pulse

systemctl --user status pipewire-pulse.service
systemctl --user restart pipewire-pulse.service
sudo systemctl --user restart pulseaudio.socket
