"""Address Conversion Utility 1.0

  Usage:
    addressconversion.py -L [-b OFFSET] [-B [-s BYTES]] (-p PHYADDR | -c CLUADDR -k CLUSECT -r RESSECT -t TABLES -f FATSECT)
    addressconversion.py -P [-b OFFSET] [-B [-s BYTES]] (-l LOGADDR | -c CLUADDR -k CLUSECT -r RESSECT -t TABLES -f FATSECT)
    addressconversion.py -C [-b OFFSET] [-B [-s BYTES]] (-l LOGADDR | -p PHYADDR)

  Options:
    -L --logical                           Calculate logical address from cluster or physical address.
    -P --physical                          Calculate physical address from cluster or logical address.
    -C --cluster                           Calculate cluster address from logical or physical address.
    -b OFFSET, --partition-start OFFSET     Specifies physical address of start partition [default: 0].
    -B, --byte-address                      Instead of returning sector values, this returns byte address.
    -s BYTES, --sector-size BYTES           Specification of bytes per sector other than default [default: 512].
    -l LOGADDR, --logical-known LOGADDR     Specifies known logical address.
    -p PHYADDR, --physical-known PHYADDR    Specifies known physical address.
    -c CLUADDR, --cluster-known CLUADDR     Specifies known cluster address.
    -k CLUSECT, --cluster-size CLUSECT      Specifies number of sectors per cluster.
    -r RESSECT, --reserved RESSECT          Specifies number of reserved sectors in partition.
    -t TABLES, --fat-tables TABLES          Specifies number of FAT tables.
    -f FATSECT, --fat-length FATSECT        Specifies length of each FAT table in sectors.

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Address Conversion Utility 1.0')
    print(arguments)

byteOffset = int(arguments['--partition-start'])
bytes = int(arguments['--sector-size'])

if arguments['--logical']:
  if arguments['--physical-known'] != None:
    physAddress = int(arguments['--physical-known'])
    if arguments['--byte-address'] == False:
      print(physAddress - byteOffset)
    elif arguments['--byte-address'] == True:
      print((physAddress - byteOffset) * bytes)
  elif arguments['--cluster-known'] != None:
    clusAddr = int(arguments['--cluster-known'])
    clusSize = int(arguments['--cluster-size'])
    reserved = int(arguments['--reserved'])
    fatTables = int(arguments['--fat-tables'])
    fatLength = int(arguments['--fat-length'])
    if arguments['--byte-address'] == False:
      print(reserved + (fatTables * fatLength) + ((clusAddr - 2) * clusSize) - byteOffset)
    elif arguments['--byte-address'] == True:
      print(bytes * (reserved + (fatTables * fatLength) + ((clusAddr - 2) * clusSize) - byteOffset))
elif arguments['--physical']:
  if arguments['--logical-known'] != None:
    logKnown = int(arguments['--logical-known'])
    if arguments['--byte-address'] == False:
      print(logKnown + byteOffset)
    elif arguments['--byte-address'] == True:
      print((logknown + byteOffset) * bytes)
  elif arguments['--cluster-known'] != None:
    clusAddr = int(arguments['--cluster-known'])
    clusSize = int(arguments['--cluster-size'])
    reserved = int(arguments['--reserved'])
    fatTables = int(arguments['--fat-tables'])
    fatLength = int(arguments['--fat-length'])
    if arguments['--byte-address'] == False:
      print(byteOffset + reserved + (fatTables * fatLength) + ((clusAddr - 2) * clusSize))
    elif arguments['--byte-address'] == True:
      print(bytes * (byteOffset + reserved + (fatTables * fatLength) + ((clusAddr - 2) * clusSize))
elif arguments['--cluster']:
  print("cluster")
  if arguments['--logical-known'] != None:
    print(arguments['--logical-known'])
    logKnown = int(arguments['--logical-known'])
    if arguments['--byte-address'] == False:

    elif arguments['--byte-address'] == True:

  elif arguments['--physical-known'] != None:
    print(arguments['--physical-known'])
     if arguments['--byte-address'] == False:

     elif arguments['--byte-address'] == True:

