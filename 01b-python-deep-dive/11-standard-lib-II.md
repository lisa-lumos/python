# 11. Brief Tour of the Standard Library - Part II
## 11.1 Output Formatting
```py
# abbreviated display of large objects
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
# "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

# pretty print
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t, width=30)
# [[[['black', 'cyan'],
#    'white',
#    ['green', 'red']],
#   [['magenta', 'yellow'],
#    'blue']]]

# wrap text
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
# The wrap() method is just like fill()
# except that it returns a list of strings
# instead of one big string with newlines
# to separate the wrapped lines.

# location/culture-specific data formatting
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# 'English_United States.1252'
conv = locale.localeconv() # get a mapping of conventions
x = 1234567.8
locale.format_string("%d", x, grouping=True)
# '1,234,567'
locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)
# '$1,234,567.80'
```

## 11.2 Templating
```py
# allow users to customize their applications,
# without having to alter the application.
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
# 'Nottinghamfolk send $10 to the ditch fund.'

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)
# Traceback (most recent call last):
#   ...
# KeyError: 'owner'
t.safe_substitute(d)
# 'Return the unladen swallow to $owner.'

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

# img_1074.jpg --> Ashley_0.jpg
# img_1076.jpg --> Ashley_1.jpg
# img_1077.jpg --> Ashley_2.jpg
```

## 11.3 Working with Binary Data Record Layouts
Loop through header information in a ZIP file without using the `zipfile` module. Pack codes "H" and "I" represent two and four byte unsigned numbers respectively. The "<" indicates that they are standard size, and in little-endian byte order:
```py
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3): # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size # skip to the next header
```

## 11.4 Multi-threading




## 11.5 Logging




## 11.6 Weak References




## 11.7 Tools for Working with Lists




## 11.8 Decimal Floating Point Arithmetic