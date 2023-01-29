#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - usb2can directory"
  exit 1
fi

#$1 usb2can directory
cd $1
git clone https://github.com/krumboeck/usb2can.git
cd usb2can

make

cd ..
dkms add -m usb2can -v 1.0 --verbose
dkms build -m usb2can -v 1.0 --verbose
dkms install -m usb2can -v 1.0 --verbose

sh setup_interface.sh
