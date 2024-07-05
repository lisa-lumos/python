# 2. Using the Python Interpreter
## 2.1 Invoking the Interpreter
```
python3.12
```
### 2.1.1 Argument Passing
The script name and additional arguments thereafter are turned into a list of strings, and assigned to the `argv` variable in the `sys` module. You can access this list by executing `import sys`.

```py
# $ python3.12 test.py 
# ['test.py']
# $ python3.12 test.py a b c
# ['test.py', 'a', 'b', 'c']
import sys
print(sys.argv)

```

### 2.1.2 Interactive Mode
```py
$ python3.12
Python 3.12 (default, April 4 2022, 09:25:04)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Continuation lines (`...`) are needed when entering a multi-line construct:
```py
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...    print("Be careful not to fall off!")
...
Be careful not to fall off!
```

## 2.2 The Interpreter and Its Environment
### 2.2.1 Source Code Encoding
By default, Python source files are treated as encoded in UTF-8. 

To declare an encoding other than the default one, a special comment line should be added as the first line of the file, except when the first line is the unix shebang line. e.g.:
```py
# -*- coding: cp1252 -*-
```
