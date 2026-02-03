sudo pacman -S speech-dispatcher

cd ~
mkdir pied
wget https://github.com/Elleo/pied/releases/pied-0.3.1-x86_64.tar.gz ~
7z x pied-0.3.1-x86_64.tar.gz
7z x pied-0.3.1-x86_64.tar
cd pied-0.3.1-x86_64
chmod +x pied
./pied
