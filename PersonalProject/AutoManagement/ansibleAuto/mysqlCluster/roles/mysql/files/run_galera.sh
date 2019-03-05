#!/bin/bash

echo "Enter scripts $0"

fileflag="/tmp/centos_galera_run"

/usr/bin/galera_new_cluster
if [ $? -ne 0 ]
then
    echo "Galera_new_cluster start failed, need check manually"
    exit 1
fi

if [ -e $fileflag ]
then
    echo "Already run galera_new_cluster"
else
    touch $fileflag
fi

echo "End script $0"

