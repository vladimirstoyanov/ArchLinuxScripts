#!/bin/sh
sudo pacman -S --noconfirm docker
sudo pacman -S --noconfirm docker-compose

sudo modprobe iptable_nat
sudo modprobe iptable_filter
sudo modprobe br_netfilter
sudo modprobe overlay

sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl status docker

#run docker without sudo
sudo usermod -aG docker $USER

echo "Testing the installation..."
docker run hello-world
