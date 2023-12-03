#!/bin/bash


ttys=$(w -h -s | awk '{print $2}')

sentences=(
    "Intrusion Alert: Unrecognized access signature detected. Initiating countermeasures to secure my rig."
    "Damn, got a snake in the system. Time to go ice-picking and flush out this intruder."
    "System Compromised: Running a deep-trace to back-hack the source of this breach."
    "Kiwi to base, we've got a leech. Deploying firewalls and preparing for a data showdown."
    "Alert: Encryption layers breached. This isn't your average script kiddie – going full net-warrior mode."
    "Hack attempt on my cyberdeck? Bad move. Reversing the flow to give them a taste of their own medicine."
    "Security Protocol: Engaged. Time to dance with the devil in the digital playground."
    "Unexpected access point opened. Diving into the net to sever their digital lifeline."
    "This intruder's good, but I'm better. Activating my custom ICE to freeze them in their tracks."
    "Net Breach: Personal device under attack. Kiwi doesn't play nice with uninvited guests."
)

num_sentences=${#sentences[@]}
random_index=$((RANDOM % num_sentences))


for tty in $ttys; do
    echo "${sentences[random_index]}"  > /dev/$tty
    #echo $val > /dev/$tty
done

