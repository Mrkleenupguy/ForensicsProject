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

# Analysis Section
# **Change filepath if img is not in the same directory
with open('TestImage1.img', 'rb') as f:
	block = f.read(48*2)
#print(block)
#print(binascii.hexlify(block))
vbr = binascii.hexlify(block[0:36*2])
for x in range(0,80,32):
	print("{} {}".format(vbr[x:x+16], vbr[x+16:x+32]))
