sudo pacman -S ollama
sudo pacman -S ollama-cuda
sudo usermod -aG video,render $USER
systemctl --user start ollama
