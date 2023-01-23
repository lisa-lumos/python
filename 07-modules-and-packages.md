# 7. Modules and Packages
PyPI is a repo for open-source third-party Python packages, which can be installed using "pip install" command. It is similar to NPM for Node.js. 

By installing Python from python.org or through the Anaconda distribution you also installed pip. 

In the terminal,
```console
lisa@mac16 ~/D/python (main)> pip install requests                 (base) 
Requirement already satisfied: requests in /Users/lisa/opt/anaconda3/lib/python3.9/site-packages (2.28.1)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/lisa/opt/anaconda3/lib/python3.9/site-packages (from requests) (1.26.11)
Requirement already satisfied: charset-normalizer<3,>=2 in /Users/lisa/opt/anaconda3/lib/python3.9/site-packages (from requests) (2.0.4)
Requirement already satisfied: idna<4,>=2.5 in /Users/lisa/opt/anaconda3/lib/python3.9/site-packages (from requests) (3.3)
Requirement already satisfied: certifi>=2017.4.17 in /Users/lisa/opt/anaconda3/lib/python3.9/site-packages (from requests) (2022.9.24)
lisa@mac16 ~/D/python (main)> pip install colorama                 (base) 
Requirement already satisfied: colorama in /Users/lisa/opt/anaconda3/lib/python3.9/site-packages (0.4.5)
lisa@mac16 ~/D/python (main)> python                               (base) 
Python 3.9.13 (main, Aug 25 2022, 18:29:29) 
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from colorama import init
>>> init()
>>> from colorama import Fore
>>> print(Fore.RED +  " some red text")
 some red text
>>> print(Fore.GREEN + "switch to green")
switch to green
>>> quit()
```

Use Google to search packages based on your needs. 
































