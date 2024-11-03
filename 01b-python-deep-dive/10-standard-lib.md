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



## 10.3 Command Line Arguments



## 10.4 Error Output Redirection and Program Termination



## 10.5 String Pattern Matching



## 10.6 Mathematics



## 10.7 Internet Access



## 10.8 Dates and Times



## 10.9 Data Compression



## 10.10 Performance Measurement



## 10.11 Quality Control



## 10.12 Batteries Included



