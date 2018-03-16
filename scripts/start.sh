#!/bin/bash

set -o nounset
set -o errexit

usage() {
	echo "Usage:" 2>&1
	echo "" 2>&1
	echo "  shell       -- Start an interactive user shell" 2>&1
	echo "  rootshell   -- Start an interactive root shell" 2>&1
	echo "  errbot      -- Start errbot" 2>&1
}

if [[ $# -lt 1 ]]; then
	usage
	exit 1
fi

cmd=$1
shift

case $cmd in
	"shell")
		cd /home/errbot
		exec runas errbot /bin/sh "$@"
		;;
	"rootshell")
    cd /root
		exec /bin/sh "$@"
		;;
	"errbot")
		cd /home/errbot
		exec runas errbot /usr/bin/errbot "$@"
		;;
	*)
		usage
		exit 1
		;;
esac
