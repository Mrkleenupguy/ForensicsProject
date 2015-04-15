"""MAC Address Conversion 1.0

Usage:
  macconv.py -T -f FILENAME
  macconv.py -T -x VAL
  macconv.py -D -f FILENAME
  macconv.py -D -x VAL

Options:
  -T  Uses time conversion module.
  -D  Uses date conversion module.
  -f FILENAME --file=FILENAME  Takes a file containing hex value to convert.
  -x VAL --hex=VAL  Takes a hex value to convert.

"""

from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Address Conversion Utility 1.0')
    print(arguments)

if arguments['-T']:
  with open('C:\Users\Jesse Laptop\Desktop\example.txt', 'r') as f:
    hexcode = f.read()
    print(hexcode)