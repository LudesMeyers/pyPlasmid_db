"""
Read all plasmid files.
Check plasmid name and existence of "Features" keyword.
Compare number of files read with number files containing "Features"

Run script from plasmid folder

""" 

import os


def getplasmidnames():

	wDir = os.getcwd() #Get path for current (plasmid) dir
	plDir = os.path.join(wDir, "plasmidFiles")
	plFiles = os.listdir(plDir) #Make list of all plasmid file names
	return(plFiles)

def parseplasmidnames(namefile):

	"""Need to index sep then split on first one"""
	for f in namefile:

		f   = f.rstrip('.gb')		
		sp  = f.find(" ")
		uds = f.find("_")
		pd  = f.find(".")

		if sp == -1 and uds == -1 and pd == -1:
			print("No Seperator in %s" % (f))
		elif sp < uds and sp < pd and sp != -1:
			ff = f.split(sep=" ", maxsplit=1)
			print(ff[0])
		elif uds < sp and uds < pd and uds != -1:
			ff = f.split(sep="_", maxsplit=1)
			print(ff[0])
		else:
			ff = f.split(sep=".", maxsplit=1)
			print(ff[0])
		

def parsesinglename(fname):

	f = fname.rstrip('.gb')
	sp = f.find(" ")
	print(sp)
	uds = f.find("_")
	print(uds)

	if sp < uds:
		ff = f.split(sep=" ", maxsplit=1)
	elif sp > uds:
		ff = f.split(sep="_", maxsplit=1)
	else:
		print("no seperator in %s" % (f))
	print("File name %s is parsed to %s" % (f, ff[0]))