#!/bin/sh
sudo pacman -S arduino arduino-cli
arduino-cli config init
arduino-cli core update-index
arduino-cli core install arduino:avr
detect_arduino.sh
