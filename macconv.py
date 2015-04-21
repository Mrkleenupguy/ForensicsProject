"""MAC Address Conversion 1.0

Usage:
  macconv.py -T (-f FILENAME | -x VAL)
  macconv.py -D (-f FILENAME | -x VAL)

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
  if arguments['--file'] != None:
    print('-T -f')
  elif arguments['--hex'] != None:
    print('-T -x')
elif arguments['-D']:
  if arguments['--file'] != None:
    print('-D -f')
  elif arguments['--hex'] != None:
    print('-D -x')