#!/bin/bash


ip=`/sbin/ifconfig eth0 | grep 'inet ' | awk '{print $2}'`
hostname=`hostname`

if ! grep -q "$ip  $hostname" /etc/hosts; then
    if grep -q "$hostname" /etc/hosts; then
        sed -i "/\b\($(hostname)\)\b/d" /etc/hosts
    fi
    echo "$ip  $hostname" >> /etc/hosts
fi
