#!/bin/bash

interface=$1
mode=$2

case $mode in
	"on")
		echo "Enable promisc mode"
		ip link set $interface down
		iw $interface set monitor control
		ip link set $interface up
		;;
	"off")
		echo "Return to managed mode"
		ip link set $interface down
		iw $interface set type managed
		ip link set $interface up
		;;

	*)
		echo "At this moment support:"
		echo "- 'monitor control'"
		echo "- 'managed'"
		;;
esac