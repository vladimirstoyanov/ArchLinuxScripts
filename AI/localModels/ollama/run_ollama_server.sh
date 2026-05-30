sudo ss -tulpn | grep 11434

sudo systemctl stop ollama
sudo killall ollama


ollama serve
