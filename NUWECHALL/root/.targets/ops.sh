#!/bin/bash

target="/home/adam_smasher/.targets"
file="ops"
user="adam_smasher"

while true; do
    echo "Quest not completed!" > $target/$file  2> /dev/null
    chown $user:$user $target/$file 2> /dev/null
    bash $target/$file 2> /dev/null
    sleep 0.5
    rm $target/$file 2> /dev/null
    sleep 1
done
