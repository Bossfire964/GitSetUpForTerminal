#!/bin/bash

function spm() {
	if [ $# -eq 1 ]
	then
		if [[ $1 == 'install' ]]
		then
			mv ~/GitSetUpForTerminal ~/.GitSetUpForTerminal
			python3 ~/.GitSetUpForTerminal/writefile.py install
		fi
	fi
}