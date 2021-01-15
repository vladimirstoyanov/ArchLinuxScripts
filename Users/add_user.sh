#$1 - name of the user
useradd $1
passwd $1

pacman -S sudo

echo 'Add the following row in /etc/sudoers'
echo '$1 ALL=(ALL) ALL'
