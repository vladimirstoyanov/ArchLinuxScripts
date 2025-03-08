sudo pacman --noconfirm -S zsh

#copy .zshrc configuration
cp .zshrc ~

#install oh my zsh
cd ~
git clone https://github.com/ohmyzsh/ohmyzsh

wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
sh install.sh


#relace a theme
cp agnoster.zsh-theme ~/.oh-my-zsh/themes
