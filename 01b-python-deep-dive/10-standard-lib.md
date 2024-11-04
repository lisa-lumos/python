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



## 10.5 String Pattern Matching



## 10.6 Mathematics



## 10.7 Internet Access



## 10.8 Dates and Times



## 10.9 Data Compression



## 10.10 Performance Measurement



## 10.11 Quality Control



## 10.12 Batteries Included



