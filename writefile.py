import sys
import os



def writeToShell():
	user = os.path.dirname(os.path.realpath(__file__)).split('/')[2]
	with open('/Users/' + user + "/.zshrc", 'a') as f:
		f.writelines(['\n'])
		f.writelines(['source ~/.GitSetUpForTerminal/commands.sh'])


def writeNew():

	user = os.path.dirname(os.path.realpath(__file__)).split('/')[2]
	writing = ["#!/bin/bash","function %s() {" % (sys.argv[1]), "\tpython3 /Users/" + user + "/Documents/" + sys.argv[1] + "/main.py $1 $2 $3 $4 $5 $6", "}"]

	with open("/Users/" + user + "/" + sys.argv[1] + ".sh", "w") as f:
		for line in writing:
			f.writelines([line + "\n"])
	with open('/Users/' + user + "/.zshrc", 'a') as f:
		f.writelines(['\n'])
		f.writelines(['source ~/' + sys.argv[1] + '.sh'])



if sys.argv[1] == "install":
	writeToShell()
else:
	writeNew()