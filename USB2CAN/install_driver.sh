#!/bin/sh

cd /usr/src
sudo git clone https://github.com/krumboeck/usb2can.git

mv usb2can/ usb2can-1.0/
cd usb2can

sudo make

cd ..
sudo dkms add -m usb2can -v 1.0 --verbose
sudo dkms build -m usb2can -v 1.0 --verbose
sudo dkms install -m usb2can -v 1.0 --verbose

sudo sh setup_interface.sh
