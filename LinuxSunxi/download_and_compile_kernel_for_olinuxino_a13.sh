#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - directory to download the linux kernel."
  exit 1
fi

cd $1

git clone https://github.com/linux-sunxi/linux-sunxi
export PATH=$(pwd)/gcc-linaro-4.9-2015.02-3-x86_64_arm-linux-gnueabihf/bin:$PATH

cp a13_linux_defconfig  $1/linux_sunxi/arch/arm/configs/
cd $1/linux_sunxi

git checkout e37d760b363888f3a65cd6455c99a75cac70a7b8

make ARCH=arm a13_linux_defconfig
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j4 uImage
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j4 INSTALL_MOD_PATH=out modules
