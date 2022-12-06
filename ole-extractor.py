#!/usr/bin/env python3
# This script reads .ole file(s) specified in argv from the terminal and extracts it


import sys
import olefile

for filename in sys.argv[1:]:
    	assert olefile.isOleFile(filename)
    	ole = olefile.OleFileIO(filename)
    	oleFiles =  (ole.listdir())
    	print(oleFiles)

    	for file in oleFiles:
            	f = open(file[0],'wb')
            	f.write(ole.openstream(file[0]).read())
            	f.close()
