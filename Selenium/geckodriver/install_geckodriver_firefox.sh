VERSION="v0.32.0" #check for the latest version at https://github.com/mozilla/geckodriver/releases/

echo "Downloading the driver..."
wget https://github.com/mozilla/geckodriver/releases/download/$VERSION/geckodriver-$VERSION-linux64.tar.gz

echo "Unziping the driver..."
tar -xzvf geckodriver-$VERSION-linux64.tar.gz

echo "Move the driver to /usr/bin/"
mv geckodriver /usr/bin/

echo "Removing the archive..."
rm geckodriver-$VERSION-linux64.tar.gz
