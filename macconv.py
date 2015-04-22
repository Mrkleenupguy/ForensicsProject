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

dir(bytes)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Address Conversion Utility 1.0')


#hex_time1 = b'53 f6';
#10:31:44
#hex_time1 = hex_time1.replace(b' ',b'');

#hex_date1 = b'42 4f';
#Feb 15, 2013
#hex_date1 = hex_date1.replace(b' ', b'');

def calctime(value):
    hex_time = value
    val1 = int(hex_time, 16)
    seconds = ((val1 & 0b11111)*2)
    minutes = ((val1 >> 5) & 0b111111)
    hours = ((val1 >> 11) & 0b11111)
    print(str(hours) + ':' + str(minutes) + ':' + str(seconds))
    return


def calcdate(value):
    hex_date = value
    val2 = int(hex_date, 16)
    day = (val2 & 0b11111)
    monthnum = ((val2 >> 5) & 0b1111)
    year = (((val2 >> 9) & 0b1111111) + 1980)
    if monthnum is 1:
        month = 'Jan'
    elif monthnum is 2:
        month = 'Feb'
    elif monthnum is 3:
        month = 'Mar'
    elif monthnum is 4:
        month = 'Apr'
    elif monthnum is 5:
        month = 'May'
    elif monthnum is 6:
        month = 'June'
    elif monthnum is 7:
        month = 'July'
    elif monthnum is 8:
        month = 'Aug'
    elif monthnum is 9:
        month = 'Sep'
    elif monthnum is 10:
        month = 'Oct'
    elif monthnum is 11:
        month = 'Nov'
    elif monthnum is 12:
        month = 'Dec'
    else:
        print('Error Calculating Month')
        return

    print(month + ' ' + str(day) + ', ' + str(year))
    return


if arguments['-T']:
    if arguments['--file'] is not None:
        with open(arguments['--file'], 'rb') as f:
            fileContents = f.read()
            calctime(fileContents)
    elif arguments['--hex'] is not None:
        calctime(arguments['--hex'])
elif arguments['-D']:
    if arguments['--file'] is not None:
        with open(arguments['--file'], 'rb') as f:
            fileContents = f.read()
            calcdate(fileContents)
    elif arguments['--hex'] is not None:
        calcdate(arguments['--hex'])
