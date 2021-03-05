import sys


def writeNew():
	writing = ["#!/bin/bash","function %s() {" % (sys.argv[1]), "\tpython3 /Users" + user + "/Documents/" + sys.argv[1] "/main.py $1 $2 $3 $4 $5 $6", "}"]

	user = os.path.dirname(os.path.realpath(__file__)).split('/')[1]
	with open("/Users/" + user + "/." + sys.argv[1]) as f:
		for line in writing:
			f.writeline(line + "\n")

def writeToShell():
	with open('~/.zshrc', 'a') as f:
		f.writeline('source ~/.GitSetUpForTerminal/commands.sh')

if sys.argv[1] == "install":
	writeToShell()
else:
	writeNew()