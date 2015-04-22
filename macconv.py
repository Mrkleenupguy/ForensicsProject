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
    
dir(bytes);

hex_time1 = b'53 f6';

hex_time1 = hex_time1.replace(b' ',b'');


print(hex_time1);

#10:31:44
val1 = int(hex_time1, 16);
print((val1 & 0b11111)*2);
print((val1 >> 5) & 0b111111);
print((val1 >> 11) & 0b11111);

hex_date1 = b'42 4f';
hex_date1 = hex_date1.replace(b' ', b'');

print(hex_date1);

#Feb 15, 2013
val2 = int(hex_date1, 16);
print(val2 & 0b11111);
print((val2 >> 5) & 0b1111);
print(((val2 >> 9) & 0b1111111) + 1980);
