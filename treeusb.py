#!/usr/bin/env python3
import sys
import os
print("Hello")
platform = sys.platform
global isLinux
isLinux = False
isMac = False
isWin = False
mountedRoot = ''

def getVersion():
	global isLinux, isMac, isWin
	print(sys.platform)
	if platform.startswith('linux'):
		isLinux = True
		return
	if platform == 'darwin':
		isMac = True
		return
	else:
		isWin = True
	return

getVersion()

while isLinux:
	print("Code not implemented... Exiting")
	mountedRoot = '/dev/'
	sys.exit(1)

while isMac:
	mountedRoot = '/Volumes/'

directories = []
dirCount = 0
filenames = []
fileCount = 0
# rootPath = mountedRoot.split('/')

def doTheWalk(mountedRoot):
	for root, dirs, files in os.walk(mountedRoot):
			if dirs:
				dirCount += 1
				directories.append(str(dirs))
			elif files:
				fileCount += 1
				filenames.append(str(files))
			print("%s contains %d Directories and %d Files" % rootPath, dirCount, fileCount)
