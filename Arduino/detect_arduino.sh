#!/bin/sh
sudo usermod -aG uucp,lock $USER

arduino-cli board search uno

arduino-cli board list
