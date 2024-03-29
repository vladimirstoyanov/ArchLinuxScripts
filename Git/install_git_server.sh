#!/bin/sh
#$1 - username

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - username"
  exit 1
fi

echo 'Update the package repository cache...'
sudo pacman -Sy --noconfirm

echo 'Installing openssh...'
sleep 1
sudo pacman --noconfirm -S openssh

echo "Enabling sshd..."
sudo systemctl enable sshd

echo "Starting OpenSSH server..."
sleep 1
sudo systemctl start sshd

echo "Checking whether OpenSSH server is running..."
sleep 1
sudo systemctl status sshd

echo "Seting-up a password-less ssh login..."
sleep 1
ssh-keygen -t rsa

echo "Coping keys to the server..."
sleep 1
cat ~/.ssh/id_rsa.pub | ssh $1@127.0.0.1 "mkdir -p ~/.ssh && cat >>  ~/.ssh/authorized_keys"
