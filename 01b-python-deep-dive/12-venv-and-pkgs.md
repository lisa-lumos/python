# 12. Virtual Environments and Packages
## 12.1 Introduction
Python applications often use packages and modules that don't come as part of the standard library. 

Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed, or the application may be written using an obsolete version of the library's interface.

A virtual environment is a self-contained directory tree, that contains a Python installation for a particular version of Python, plus a number of additional packages.

Different applications can then use different virtual environments. 

## 12.2 Creating Virtual Environments
`venv` will install the Python version from which the command was run. A common directory location for a virtual environment is ".venv", which keeps the directory hidden in your shell, and thus out of the way. 

```sh
cd [path-to-venv]
python -m venv tutorial-env

source tutorial-env/bin/activate

deactivate
```

## 12.3 Managing Packages with pip

