cmd_/home/buildslave/workspace/BinaryRelease/label/hetzner/target/arm-linux-gnueabihf/_build/sysroots/arm-linux-gnueabihf/usr/include/linux/netfilter_arp/.install := /bin/bash scripts/headers_install.sh /home/buildslave/workspace/BinaryRelease/label/hetzner/target/arm-linux-gnueabihf/_build/sysroots/arm-linux-gnueabihf/usr/include/linux/netfilter_arp ./include/uapi/linux/netfilter_arp arp_tables.h arpt_mangle.h; /bin/bash scripts/headers_install.sh /home/buildslave/workspace/BinaryRelease/label/hetzner/target/arm-linux-gnueabihf/_build/sysroots/arm-linux-gnueabihf/usr/include/linux/netfilter_arp ./include/linux/netfilter_arp ; /bin/bash scripts/headers_install.sh /home/buildslave/workspace/BinaryRelease/label/hetzner/target/arm-linux-gnueabihf/_build/sysroots/arm-linux-gnueabihf/usr/include/linux/netfilter_arp ./include/generated/uapi/linux/netfilter_arp ; for F in ; do echo "\#include <asm-generic/$$F>" > /home/buildslave/workspace/BinaryRelease/label/hetzner/target/arm-linux-gnueabihf/_build/sysroots/arm-linux-gnueabihf/usr/include/linux/netfilter_arp/$$F; done; touch /home/buildslave/workspace/BinaryRelease/label/hetzner/target/arm-linux-gnueabihf/_build/sysroots/arm-linux-gnueabihf/usr/include/linux/netfilter_arp/.install
