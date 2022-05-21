echo "Installing apache package..."
pacman -S apache
sleep 1

echo "Installing php..."
pacman -S php php-apache
sleep 1

cp httpd.conf /etc/httpd/conf/

systemctl restart httpd.service

echo "Information: /var/www/ is replaced by /srv/httpd/"
