#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - directory to download the linux kernel."
  exit 1
fi

CURRENT_DIRECTORY=$(pwd)

cd $1

echo "=======Downloading the compiler..."
wget https://releases.linaro.org/archive/15.02/components/toolchain/binaries/arm-linux-gnueabihf/gcc-linaro-4.9-2015.02-3-x86_64_arm-linux-gnueabihf.tar.xz

echo "======Extracting the compiler..."
tar -xvf gcc-linaro-4.9-2015.02-3-x86_64_arm-linux-gnueabihf.tar.xz



echo "======Clonign linux-sunxi directory..."
git clone https://github.com/linux-sunxi/linux-sunxi
export PATH=$(pwd)/gcc-linaro-4.9-2015.02-3-x86_64_arm-linux-gnueabihf/bin:$PATH

echo "$CURRENT_DIRECTORY"
cp $CURRENT_DIRECTORY/a13oLinuxino/a13_linux_defconfig  $1/linux-sunxi/arch/arm/configs/
cd $1/linux-sunxi

echo "======Checkout 3.4.90+ commit..."
git checkout e37d760b363888f3a65cd6455c99a75cac70a7b8

echo "=====Configuring the kernel..."
make ARCH=arm a13_linux_defconfig

echo "=====Building the kernel..."
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j4 uImage
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j4 INSTALL_MOD_PATH=out modules
