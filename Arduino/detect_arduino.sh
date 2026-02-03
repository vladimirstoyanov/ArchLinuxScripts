#!/bin/sh
sudo usermod -aG uucp,lock $USER

if ls /dev/ttyACM* >/dev/null 2>&1; then
    echo "Arduino detected"
else
    echo "No Arduino"
fi
