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
	if [ $# -eq 3 ]
	then
		cd ~
		mkdir ~/.tempdelete
		cd ~/.tempdelete 
		git clone $3
		for file in ~/.tempdelete/*
		do
			mv $file ~/Documents/$2
			rm -rf ~/.tempdelete
		done
		cd ~
		touch $2.sh
		python3 ~/.GitSetUpForTerminal/writefile.py $2
	fi
}