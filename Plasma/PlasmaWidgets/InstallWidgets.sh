echo "Adding printVulnearablePackages.sh on boot time..."
python2.7 ../Systemd/start_binary_at_boot_time.py printVulnearablePackages '$(pwd)/BootTimeScripts/printVulnearablePackages.sh $(pwd)' 'print vulnearable packages'
sleep 1

echo "Installing vulnearable packages plasma widget"
sh Plasma/install_widget.sh Plasma/PlasmaWidgets/Vulnerable_packages/
sleep 1

echo "Adding currentConnectedIpAddresses.sh on boot time..."
python2.7 ../Systemd/start_binary_at_boot_time.py current_connected_ip_addresses '$(pwd)/BootTimeScripts/currentConnectedIpAddresses.sh' 'list of connected ip addresses'
sleep 1

echo "Installing current connected ip addresses  plasma widget"
sh Plasma/install_widget.sh Plasma/PlasmaWidgets/Current_connected_ip_addresses/
sleep 1

echo "Adding getCurrencies.sh on boot time..."
python2.7 ../Systemd/start_binary_at_boot_time.py get_currencies '$(pwd)/BootTimeScripts/getCurrencies.sh $(pwd)' 'Currencies rates'
sleep 1

echo "Installing currencies plasma widget"
sh Plasma/install_widget.sh Plasma/PlasmaWidgets/curriences_rates/
sleep 1
