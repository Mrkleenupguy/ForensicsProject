__author__ = 'Jesse'

import hashlib
import binascii

md5hash = hashlib.md5()
sha1hash = hashlib.sha1()

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
# Analysis Section
# **Change filepath if img is not in the same directory
with open('C:\Users\John Jesse\Desktop\TestImage1.img', 'rb') as f:
	block = f.read(512)
	byteblock = binascii.hexlify(block)
#vbr = binascii.hexlify(block[0:80])
#for x in range(0,80,32):
#	print("{} {}".format(vbr[x:x+16], vbr[x+16:x+32]))