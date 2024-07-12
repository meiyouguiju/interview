#!/bin/bash

# 磁盘列表
disks=("sda" "sdb" "sdc")

for disk in ${disks[@]}
do
    echo "正在处理磁盘：$disk"

    # 获取分区列表
    partitions=$(ls /dev | grep "^$disk[0-9]*$")

    for part in $partitions
    do
        echo "正在删除分区：/dev/$part"
        # 卸载分区
        umount /dev/$part
        # 删除分区
        echo -e "d\nw" | fdisk /dev/$disk
    done
done
