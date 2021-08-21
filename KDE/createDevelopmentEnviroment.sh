#For more information: https://community.kde.org/Get_Involved/development
#$1 - username git
#$2 - email git

echo "=======Installing basic packages"
#sudo pacman sudo pacman -S git cmake dialog

echo "=======Configuring git"
#git config --global user.name $1
#git config --global user.email $2

echo "======Setting-up kdesrc-build"
#mkdir -p ~/kde/src
cd ~/kde/src/
#git clone https://invent.kde.org/sdk/kdesrc-build.git && cd kdesrc-build

#./kdesrc-build --initial-setup
#source ~/.bashrc


echo "======Building plasma"
./kdesrc-build/kdesrc-build plasma-workspace plasma-framework plasma-nm plasma-pa plasma-thunderbolt plasma-vault plasma-firewall plasma-workspace-wallpapers kdeplasma-addons krunner milou kwin kscreen sddm-kcm plymouth-kcm breeze discover print-manager plasma-sdk kaccounts-integration kaccounts-providers kdeconnect-kde plasma-browser-integration xdg-desktop-portal-kde kde-gtk-config khotkeys kgamma5 breeze-gtk --include-dependencies

echo "======Building plasma-desktop" 
./kdesrc-build/kdesrc-build plasma-desktop systemsettings ksysguard plasma-disks plasma-systemmonitor ksystemstats kinfocenter kmenuedit --include-dependencies






