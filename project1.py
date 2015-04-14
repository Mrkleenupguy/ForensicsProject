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
			   '3c':'Partition Magic Recovery Partition'}

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

def partitionEntry(entry):
	"Displays parition entry information"
	print(binascii.hexlify(entry[0]))
	print(binascii.hexlify(entry[1]))
	print(binascii.hexlify(entry[2:4]))
	print(filesystems[binascii.hexlify(entry[4])])
	print(binascii.hexlify(entry[5]))
	print(binascii.hexlify(entry[6:8]))
	print(binascii.hexlify(entry[11:7:-1]))
	print(binascii.hexlify(entry[15:11:-1]))
	return

# Analysis Section
# **Change filepath if img is not in the same directory
with open('C:\Users\Jesse Laptop\Desktop\TestImage1.img', 'rb') as f:
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