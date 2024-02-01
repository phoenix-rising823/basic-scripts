#!/bin/bash
#set -xv

clear
data_arch=$(ls /mnt/data)
dat_dest="/mnt/"
cd /mnt/data
for dat in $data_arch
do
	echo "Archiving $dat..."
	tar czf "${dat_dest}${dat}_$(date +%F_%R).tar.gz" $dat
	echo "${dat} archive complete!!"
	echo "Syncing ${dat} archive..."
	rsync -az "${dat_dest}${dat}_$(date +%F_%R).tar.gz" user@host:/mnt/backup
done


echo "All archives created!!"
echo "Test created archives to ensure validity."

