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
    -s BYTES, --sector-size BYTES           Specification of bytes per sector other that default 512.
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

if arguments['--logical']:
  print("logical")
  if arguments['--physical-known'] != None:
    physAddress = int(arguments['--physical-known'])
    print(physAddress - byteOffset)
  elif arguments['--cluster-known'] != None:
    print(arguments['--cluster-known'])
    clusAddr = int(arguments['--cluster-known'])
    clusSize = int(arguments['--cluster-size'])
    reserved = int(arguments['--reserved'])
    fatTables = int(arguments['--fat-tables'])
    fatLength = int(arguments['--fat-length'])
elif arguments['--physical']:
  print("physical")
  if arguments['--logical-known'] != None:
    print(arguments['--logical-known'])
  elif arguments['--cluster-known'] != None:
    print(arguments['--cluster-known'])
    clusAddr = int(arguments['--cluster-known'])
    clusSize = int(arguments['--cluster-size'])
    reserved = int(arguments['--reserved'])
    fatTables = int(arguments['--fat-tables'])
    fatLength = int(arguments['--fat-length'])
    result = byteOffset + reserved + (fat-tables * fat-length) + ((clusAddr - 2) * clusSize)
    print(result)
elif arguments['--cluster']:
  print("cluster")