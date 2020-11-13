CURRENT_DIR=$(pwd)
HOME_PATH=~
REPOSITORY=https://github.com/N3TC4T/Nearby-Live-Desktop.git
NEARBY_PATH=~/Nearby-Live-Desktop/


cd $HOME_PATH

rm -rf Nearby-Live-Desktop/
git clone $REPOSITORY

cp $CURRENT_DIR/npm-shrinkwrap.json $NEARBY_PATH
cp $CURRENT_DIR/package.json $NEARBY_PATH
cd $NEARBY_PATH

npm install
gulp dev




