__author__ = 'Jesse'

import hashlib
import binascii

md5hash = hashlib.md5()
sha1hash = hashlib.sha1()
filesystems = {'01':'DOS 12-BIT FAT',
			   '04':'DOS 16-BIT FAT for partitions smaller than 32 MB',
			   '05':'Extended Partition',
			   '06':'DOS 16-BIT FAT for partitions larger than 32 MB',
			   '07':'NTFS',
			   '08':'AIX Bootable Partition',
			   '09':'AIX Data Partition',
			   '0b':'DOS 32-BIT FAT',
			   '0c':'DOS 32-BIT FAT for interrupt 13 support',
			   '17':'Hidden NTFS Parition (XP and earlier',
			   '1b':'Hidden FAT32 Partition',
			   '1e':'Hidden VFAT Partition',
			   '3c':'Partition Magic Recovery Partition',
			   '66':'Novell',
			   '67':'Novell',
			   '68':'Novell',
			   '69':'Novell',
			   '81':'Linux',
			   '82':'Linux swap parition (can also be associated with Solaris partitions)',
			   '83':'Linux native file systems (Ext2, Ext3, Reiser, xiafs)'}

# Filepath is hard coded to cut down on test time
#filepath = input("Enter file path: ")
#print(filepath)

# MD5 SHA1 hash section commented out to cut down on run time while
# working on analysis section
"""
with open('TestImage1.img', 'rb') as f:
    fileContents = f.read(512)
    md5hash.update(fileContents)
    sha1hash.update(fileContents)
print(md5hash.hexdigest())
print(sha1hash.hexdigest())
"""

startSectors = [];
partitionTypes = [];

def partitionEntry(entry):
	"Displays parition entry information"
	#print(binascii.hexlify(entry[0])) #Current State of Partition
	#print(binascii.hexlify(entry[1])) #Beginning of Partition - Head
	#print(binascii.hexlify(entry[2:4])) #Beginning of Partition -Cylinder/Sector
	#print(int(binascii.hexlify(entry[2:4]), 16))
	partType = filesystems[binascii.hexlify(entry[4])] #Type of Partition
	partitionTypes.append(partType)
	#print(binascii.hexlify(entry[5])) #End of Partition - Head
	#print(binascii.hexlify(entry[6:8])) #End of Partition - Cylinder/Sector
	#print(int(binascii.hexlify(entry[6:8]), 16))
	startSectorAddr = int(binascii.hexlify(entry[11:7:-1]), 16)
	startSectors.append(startSectorAddr);
	sectorSize = int(binascii.hexlify(entry[15:11:-1]), 16)
	print("({}) {}, {}, {}".format(binascii.hexlify(entry[4]), partType, startSectorAddr, sectorSize))
	return

def vbrAnalysis(vbr, partNum):
	"Displays VBR information"
	OEMNAME = binascii.hexlify(vbr[3:11])
	bytesPerSector = int(binascii.hexlify(vbr[12:10:-1]), 16)
	sectorsPerCluster = int(binascii.hexlify(vbr[13]), 16)
	resSize = int(binascii.hexlify(vbr[15:13:-1]), 16)
	numOfFATS = int(binascii.hexlify(vbr[16]), 16)
	maxFiles = int(binascii.hexlify(vbr[18:16:-1]), 16)
	sizeOfFS = int(binascii.hexlify(vbr[20:18:-1]), 16)
	sizeOfFAT = int(binascii.hexlify(vbr[23:21:-1]), 16)
	sizeOfFS32 = int(binascii.hexlify(vbr[35:31:-1]) ,16)
	sizeOfFAT32 = int(binascii.hexlify(vbr[39:35:-1]), 16)

	print('Partition {}({}):'.format(partNum, partitionTypes[x]))
	print('Reserved area: Start sector: 0 Ending sector: {} Size: {}'.format(resSize-1, resSize))
	print('Sectors per cluster: {}'.format(sectorsPerCluster))
	if (sizeOfFAT == 0):
		print('FAT area: Start sector: {} Ending sector: {}'.format(resSize, resSize+(sizeOfFAT32*2)-1))
	else:
		print('FAT area: Start sector: {} Ending sector: {}'.format(resSize, resSize+(sizeOfFAT*2)-1))
	print('Number of FATs: {}'.format(numOfFATS))
	if (sizeOfFAT == 0):
		print('The size of each FAT: {}'.format(sizeOfFAT32))
	else:
		print('The size of each FAT: {}'.format(sizeOfFAT))
	print('The first sector cluster 2: ')
	return

# Analysis Section
# **Change filepath if img is not in the same directory
with open('C:\Users\John Jesse\Desktop\TestImage1.img', 'rb') as f:
	diskImg = f.read()
	#otherblock = f.read()
executionCode = diskImg[0:446] # this is just code that used to boot up, probably won't use this
firstPartition = diskImg[446:462] 
secondPartition = diskImg[462:478]
thirdPartiion = diskImg[478:494]
fourthPartiion = diskImg[494:510]
brs = diskImg[510:512]

partitionEntry(firstPartition)
partitionEntry(secondPartition)
partitionEntry(thirdPartiion)
partitionEntry(fourthPartiion)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
for x in range(0, len(startSectors)):
	#print(binascii.hexlify(diskImg[(startSectors[x])*512:(startSectors[x]+1)*512]))
	vbrAnalysis(diskImg[(startSectors[x])*512:(startSectors[x]+1)*512], x)
	print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')