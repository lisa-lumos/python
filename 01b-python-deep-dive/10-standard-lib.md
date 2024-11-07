# 10. Brief Tour of the Standard Library
## 10.1 Operating System Interface
The `os` module provides functions for interacting with the operating system:
```py
import os
os.getcwd()      # Return the current working directory
# 'C:\\Python312'

os.chdir('/server/access_logs')   # Change current working directory

os.system('mkdir today')   # Run the command mkdir in the system shell

dir(os) # <returns a list of all module functions>
help(os) #<returns an extensive manual page created from the module's docstrings>

```

For daily file and directory management tasks, the `shutil` module:
```py
import shutil
shutil.copyfile('data.db', 'archive.db') # 'archive.db'
shutil.move('/build/executables', 'install_dir') # 'install_dir'

```

## 10.2 File Wildcards
The `glob` module - making file lists from directory wildcard searches:
```py
import glob
glob.glob('*.py') # ['primes.py', 'random.py', 'quote.py']
```

## 10.3 Command Line Arguments
Common utility scripts often need to process command line arguments. These arguments are stored in the `sys` module's `argv` attribute, as a list. 

File "demo.py":
```py
import sys
print(sys.argv)
```

In the command line:
```sh
python demo.py one two three
# ['demo.py', 'one', 'two', 'three']
```

The `argparse` module provides a better mechanism to process command line arguments. The following script extracts one or more filenames and an optional number of lines:
```py
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file'
)
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```
When run at the command line with `python top.py --lines=5 alpha.txt beta.txt`, the script sets `args.lines` to `5` and `args.filenames` to `['alpha.txt', 'beta.txt']`.


## 10.4 Error Output Redirection and Program Termination
The `sys` module has attributes for `stdin`, `stdout`, and `stderr`. The latter is useful for emitting warnings and error messages, to make them visible, even when `stdout` has been redirected:

```py
sys.stderr.write('Warning, log file not found starting a new one\n')
# Warning, log file not found starting a new one
```

The most direct way to terminate a script is to use `sys.exit()`.

## 10.5 String Pattern Matching
```py
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# ['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
# 'cat in the hat'

# for simple use cases, string methods are preferred,
# because they are easier to read/debug
'tea for too'.replace('too', 'two')
# 'tea for two'

```

## 10.6 Mathematics
skip


## 10.7 Internet Access
```py
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode() # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip()) # Remove trailing newline
            # datetime: 2022-01-01T01:36:47.689215+00:00

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('sender@example.org', 'receiver@example.org',
"""To: receiver@example.org
From: sender@example.org

Beware the Ides of March.
""")
server.quit()
```

## 10.8 Dates and Times
The module also supports objects that are timezone aware.
```py
from datetime import date
now = date.today()
now # datetime.date(2003, 12, 2)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days
14368
```

## 10.9 Data Compression



## 10.10 Performance Measurement



## 10.11 Quality Control



## 10.12 Batteries Included



