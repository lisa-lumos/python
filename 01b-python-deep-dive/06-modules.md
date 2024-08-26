# 6. Modules
As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you've written in several programs without copying its definition into each program.

To support this, Python has a way to put definitions in a file and use them elsewhere - a module. definitions from a module can be imported into other modules, or into the main module.

The file name is the module name with the suffix .py appended. Within a module, the module's name (as a string) is available as the value of the global variable `__name__`.

## 6.1 More on Modules
A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement.

Each module has its own private namespace, which is used as the global namespace by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user's global variables. You can touch a module's global variables with the same notation used to refer to its functions - `module_name.item_name`.

```py
import my_module # my_module.my_function()

import my_module as mdl # mdl.my_function()

from my_module import my_function # my_function()

from my_module import my_function as my_func # my_func()

from my_module import * # discouraged to use this, may introduce unknown names to code, and not readable

```

### 6.1.1 Executing modules as scripts
by adding this code at the end of your module:
```py
if __name__ == "__main__": # only runs if the script is passed to python cmd
    import sys
    fib(int(sys.argv[1]))
```
you can make the file usable as a script as well as an importable module.

This is often used either to provide a convenient UI to a module, or for testing purposes (running the module as a script).

### 6.1.2 The Module Search Path
When a module named "spam" is imported, the interpreter first searches for a built-in module with that name. These module names are listed in `sys.builtin_module_names`. If not found, it then searches for a file named "spam.py" in a list of directories given by the var `sys.path`. 

`sys.path` is initialized from these locations:
- The dir containing the input script (or the current dir when no file is specified).
- `PYTHONPATH` (a list of dir names, with the same syntax as the shell variable PATH).
- The installation-dependent default (by convention including a `site-packages` dir, handled by the site module).

### 6.1.3 "Compiled" Python files
To speed up loading modules, Python caches the compiled version of each module in the "__pycache__/module.version.pyc" file. 

Python checks the modification date of the source against the compiled version to see if it's out of date and needs to be recompiled. This is a completely automatic process. 

The compiled modules are `platform-independent`, so the same library can be shared among systems with different architectures.

To support a non-source (compiled only) distribution, the compiled module must be in the source directory, and there must not be a source module.

## 6.2 Standard Modules
The variable `sys.path` is a list of strings that determines the interpreter's search path for modules. It is initialized to a default path taken from the environment variable "PYTHONPATH", or from a built-in default if "PYTHONPATH" is not set. You can modify it using standard list operations:
```py
import sys
sys.path.append('/ufs/guido/lib/python')
```

## 6.3 The dir() Function
The built-in function `dir(module_name)` is used to find out which names a module defines. It returns a sorted list of strings:
```py
import fibo, sys
dir(fibo)
# ['__name__', 'fib', 'fib2']
dir(sys)  
# ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
#  '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
#  '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
#  '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
#  '_getframe', '_git', '_home', 
```

Without arguments, `dir()` lists the names you have defined currently.

`dir()` does not list the names of built-in functions and variables. If you want a list of those, they are defined in the standard module "builtins".

## 6.4 Packages
### 6.4.1 Importing * From a Package
### 6.4.2 Intra-package References
### 6.4.3 Packages in Multiple Directories

















