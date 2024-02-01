#!/bin/bash
#set -xv

data_rest=$(ls /mnt/rest)
dat_rest="/mnt/data/"
cd /mnt/rest
rsync -avz --progress user@host:/mnt/backup/ $data_rest
for d in $data_rest
do
 echo "Restoring ${d}..."
 tar xf ${d} -C ${dat_rest}
 echo "Restore of ${d} complete!!"
done

echo "Data restored to ${dat_rest}"
echo "Verify the restoration now"
