echo "Installing nmap..."
pacman -S nmap

echo "Installing dolphin (kde file manager)..."
pacman -S dolphin

echo "Installing kwrite..."
pacman -S kwrite

echo "Installing iptables..."
pacman -S iptables

echo "Installing conntrack-tools (it is using by iptables)..."
pacman -S conntrack-tools

echo "Installing wget..."
pacman -S wget

echo "Installing wifi packages, network manager..."
pacman -S wpa_supplicant  wireless_tools networkmanager network-manager-applet gnome-keyring

echo "Installing wireless_tools..."
pacman -S wireless_tools

echo "Installing net-tools..."
pacman -S net-tools

echo "Installing konsole..."
pacman -S konsole

echo "Installing virtualbox..."
pacman -S virtualbox

echo "Installing firefox..."
pacman -S firefox

echo "Installing tcpdump..."
pacman -S tcpdump

echo "Installing whois..."
pacman -S whois

echo "Installing hexchat (IRC client)..."
pacman -S hexchat

echo "Installing python-pip..."
pacman -S python-pip

echo "Installing numpy..."
pip install numpy

echo "Installing scipy..."
pip install scipy

echo "Installing scikit-learn..."
pip install scikit-learn

echo "Installing matplotlib..."
pip install matplotlib

echo "Installing selenium..."
pip install selenium

echo "Installing mechanize..."
pip install mechanize

echo "Installing atom editor..."
pacman -S atom

echo "Installing tensorflow..."
pip install tensorflow
