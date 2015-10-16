#!/usr/bin/env python3
import sys
import os
import maker
import pprint

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
	elif platform == 'darwin':
		isMac = True
		return
	elif platform == 'win32':
		isWin = True
		return
	else:
		return("Can't Get System Version")

def doTheWalk(mountedRoot):
	directories = []
	dirCount = 0
	filenames = []
	fileCount = 0
	for root, dirs, files in os.walk(mountedRoot):
		if dirs:
			dirCount += 1
			directories.append(str(dirs))
		elif files:
			fileCount += 1
			filenames.append(str(files))

	print(directories)
	#print("%s contains %d Directories and %d Files" % (mountedRoot, dirCount, fileCount))
	#print(mountedRoot)
	#for d in directories: print("%s" % str(d))
	#for f in filenames: print("%s" % str(f))

getVersion()

if isLinux:
	username = os.getenv('USER')
	mountedRoot = '/media/' + username
	contents = os.listdir(mountedRoot)
	print("Which drive to enumerate: \n")
	num = input(str(list(enumerate(os.listdir(mountedRoot)))) + '\n\n')
	newPath = mountedRoot + '/' + contents[int(num)]
	print("\n Enumerating " + contents[int(num)] + ' ... ')
	print(newPath)
	#doTheWalk(newPath)
	print((maker.FileTreeMaker().make(newPath)))

while isMac:
	mountedRoot = '/Volumes/'

# rootPath = mountedRoot.split('/')
