__author__ = 'Jesse'

import hashlib
import binascii

md5hash = hashlib.md5()
sha1hash = hashlib.sha1()
filesystems = {'01':'DOS 12-BIT FAT',
			   '04':'DOS 16-BIT FAT',
			   '05':'Extended Partition',
			   '06':'DOS 16-BIT FAT',
			   '07':'NTFS',
			   '08':'AIX Bootable Partition',
			   '09':'AIX Data Partition',
			   '0b':'DOS 32-BIT FAT',
			   '0c':'DOS 32-BIT FAT',
			   '17':'Hidden NTFS Parition (XP and earlier',
			   '1b':'Hidden FAT32 Partition',
			   '1e':'Hidden VFAT Partition',
			   '3c':'Partition Magic Recovery Partition',
			   '66':'Novell',
			   '67':'Novell',
			   '68':'Novell',
			   '69':'Novell'}

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
def fromLittleEndian(bytes):
	""
	result = ""
	for i in range(0,len(bytes),2):
		result = result + bytes[i+1] + bytes[i]
	return result[::-1]

def mbrAnalysis(mbr):
	return

def partitionEntry(entry):
	"Displays parition entry information"
	print(binascii.hexlify(entry[0])) #Current State of Partition
	print(binascii.hexlify(entry[1])) #Beginning of Partition - Head
	print(binascii.hexlify(entry[2:4])) #Beginning of Partition -Cylinder/Sector
	partType = filesystems[binascii.hexlify(entry[4])] #Type of Partition
	print(binascii.hexlify(entry[5])) #End of Partition - Head
	print(binascii.hexlify(entry[6:8])) #End of Partition - Cylinder/Sector
	startSector = int(binascii.hexlify(entry[11:7:-1]), 16)
	sectorSize = int(binascii.hexlify(entry[15:11:-1]), 16)
	print("({}) {}, {}, {}".format(binascii.hexlify(entry[4]), partType, startSector, sectorSize))
	return

# Analysis Section
# **Change filepath if img is not in the same directory
with open('C:\Users\John Jesse\Desktop\TestImage1.img', 'rb') as f:
	block = f.read(512)
executionCode = block[0:446]
firstPartition = block[446:462]
secondPartition = block[462:478]
thirdPartiion = block[478:494]
fourthPartiion = block[494:510]
brs = block[510:512]

print(binascii.hexlify(firstPartition))
print(binascii.hexlify(secondPartition))
print(binascii.hexlify(thirdPartiion))
print(binascii.hexlify(fourthPartiion))
print(binascii.hexlify(brs))
partitionEntry(firstPartition)
partitionEntry(secondPartition)
partitionEntry(thirdPartiion)
partitionEntry(fourthPartiion)