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
Threads can be used to improve the responsiveness of applications that accept user input, while other tasks run in the background. A related use case is running I/O, in parallel with computations in another thread.
```py
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

```

The principal challenge of multi-threaded applications is coordinating threads that share data or other resources. To that end, the threading module provides a number of synchronization primitives, including locks, events, condition variables, and semaphores.

While those tools are powerful, minor design errors can result in problems that are difficult to reproduce. So, the preferred approach to task coordination, is to concentrate all access to a resource in a single thread and then use the queue module to feed that thread with requests from other threads. Applications using Queue objects for inter-thread communication and coordination are easier to design, more readable, and more reliable.

## 11.5 Logging
By default, informational and debugging messages are suppressed, and log messages are sent to a file or to `sys.stderr`. Other output options include routing messages through email, datagrams, sockets, or to an HTTP Server.
```py
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
# WARNING:root:Warning:config file server.conf not found
logging.error('Error occurred')
# ERROR:root:Error occurred
logging.critical('Critical error -- shutting down')
# CRITICAL:root:Critical error -- shutting down
```

The logging system can be configured directly from Python, or can be loaded from a user editable configuration file for customized logging without altering the application.

## 11.6 Weak References
The memory for an object is freed shortly after the last reference to it has been eliminated. Occasionally there is a need to track objects only as long as they are being used by something else, which creates a reference that makes them permanent. The `weakref` module provides tools for tracking objects without creating a reference. 

Typical applications include caching objects that are expensive to create:
```py
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10) # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a # does not create a reference
d['primary'] # fetch the object if it is still alive
# 10
del a # remove the one reference
gc.collect() # run garbage collection right away
# 0
d['primary'] # entry was automatically removed
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     d['primary']                # entry was automatically removed
#   File "C:/python312/lib/weakref.py", line 46, in __getitem__
#     o = self.data[key]()
# KeyError: 'primary'
```

## 11.7 Tools for Working with Lists




## 11.8 Decimal Floating Point Arithmetic