__author__ = 'Jesse'

import hashlib
import binascii
import os

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
			   '83':'Linux native file systems (Ext2, Ext3, Reiser, xiafs)',
			   '86':'FAT 16 volume/stripe set (Windows NT)',
			   '87':'High Performance File System (HPFS) fault-tolerant mirrored partition or NTFS volme/stripe set',
			   'A5':'FreeBSD and BSD/386',
			   'A6':'OpenBSD',
			   'A9':'NetBSD',
			   'C7':'Typical of a corrupted NTFS volume/stripe set',
			   'EB':'BeOS'}

startSectors = [];
partitionTypes = [];

def partitionEntry(entry):
	"Displays parition entry information"
	partType = filesystems[binascii.hexlify(entry[4])] #Type of Partition
	partitionTypes.append(partType)
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
		print('Number of FATs: {}'.format(numOfFATS))
		print('The size of each FAT: {}'.format(sizeOfFAT32))
		print('The first sector cluster 2: {}'.format(resSize+(sizeOfFAT32*2)+startSectors[partNum]))
	else:
		print('FAT area: Start sector: {} Ending sector: {}'.format(resSize, resSize+(sizeOfFAT*2)-1))
		print('Number of FATs: {}'.format(numOfFATS))
		print('The size of each FAT: {}'.format(sizeOfFAT))
		print('The first sector cluster 2: {}'.format(resSize+(sizeOfFAT*2)+startSectors[partNum]+((maxFiles*32)/bytesPerSector)))
	return

"""

"""

# Analysis Section
filename = raw_input('Enter file path: ')
newFileName = os.path.basename(filename).split('.')[0]
filePath = os.path.dirname(filename) + '\\'
sha1FileName = 'MD5-' + newFileName + '.txt'
md5FileName = 'SHA-' + newFileName + '.txt'

with open(filename, 'rb') as f:
    fileContents = f.read()
    md5hash.update(fileContents)
    sha1hash.update(fileContents)
md5digest = md5hash.hexdigest()
shadigest = sha1hash.hexdigest()

# Hash results are stored in separate text files, but they are
# in the same directory as the disk image file
with open((filePath + sha1FileName), 'w') as sha1File:
	sha1File.write(shadigest)
with open((filePath + md5FileName), 'w') as md5File:
	md5File.write(md5digest)


with open(filename, 'rb') as f:
	diskImg = f.read()
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
	if (partitionTypes[x] == filesystems['04'] or partitionTypes[x] == filesystems['06'] or
		 partitionTypes[x] == filesystems['0b'] or partitionTypes[x] == filesystems['0c']):
		vbrAnalysis(diskImg[(startSectors[x])*512:(startSectors[x]+1)*512], x)
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')