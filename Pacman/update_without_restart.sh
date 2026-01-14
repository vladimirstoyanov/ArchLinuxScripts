#!/bin/sh

LOG=/var/log/auto-update.log

echo "===== $(date) =====" >> "$LOG"

# ensure /boot is mounted
if ! mountpoint -q /boot; then
    mount /boot >> "$LOG" 2>&1
fi

# safety: prevent concurrent pacman
if [ -e /var/lib/pacman/db.lck ]; then
    echo "pacman is locked, skipping" >> "$LOG"
    exit 0
fi

pacman -Syu --noconfirm >> "$LOG" 2>&1

# FAILSAFE: always rebuild initramfs
mkinitcpio -P >> "$LOG" 2>&1

sync
echo "Update finished" >> "$LOG"
