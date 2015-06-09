#!/usr/bin/env python

import sys
import os
import shutil
import subprocess

if len(sys.argv) != 2:
	print "Usage: %s <prefix>"
	sys.exit(-1)

prefix = sys.argv[1]

conversion_table = {
	".gtl": "-F_Cu.gbr",	# Top layer
	".gbl": "-B_Cu.gbr",	# Bottom layer
	".gto": "-F_SilkS.gbr",	# Silk Top
	".gbo": "-B_SilkS.gbr", # Silk Bottom
	".gts": "-F_Mask.gbr",	# Solder Stop Mask Top
	".gbs": "-B_Mask.gbr",	# Solder Stop Mask Bottom
	".gko": "-Edge_Cuts.gbr",	# Outline layer
	".gtp": "-F_Paste.gbr",	# Top paste
	".gbp": "-B_Paste.gbr",	#Bottom Paste
	".g2l": "-In1_Cu.gbr",	# Top paste
	".g3l": "-In2_Cu.gbr",	#Bottom Paste
	".xln": ".drl",			# NC Drill
}

files = []

for key in conversion_table:
	srcfile = '%s%s' % (prefix, conversion_table[key])
	dstfile = '%s%s' % (prefix, key)

	if os.path.isfile(srcfile):
		shutil.copy(srcfile, dstfile)
		files.append(dstfile)

zip_itead_extensions = [".gtl", ".gbl", ".gto", ".gbo", ".gts", ".gbs", ".gko", ".xln", ".g2l", ".g3l"];

zip_itead = []

for extension in zip_itead_extensions:
	filename = '%s%s' % (prefix, extension)

	if not os.path.isfile(filename):
		print "File '%s' does not exists!" % filename

	zip_itead.append(filename)

if os.path.isfile("%s.zip" % (prefix)):
	os.remove("%s.zip" % (prefix))

if len(zip_itead) == len(zip_itead_extensions):
	# zip stuff
	args = ["zip", "%s.zip" % (prefix)]
	args.extend(zip_itead)
	subprocess.call(args)
