#!/bin/sh
script -q -c "pacman -Suy --noconfirm" /dev/null

script -q -c "pacman --noconfirm --disable-hooks=90-mkinitcpio-install.hook -S linux linux-firmware linux-headers" /dev/null


mkinitcpio -P
