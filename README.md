# Python Notes
Python focuses on optimizing developer time, rather than a computer's processing time. It has documentation at `docs.python.org/3`. 

Python can automate simple tasks: 
- Search for files and editing them
- Scraping info from a website
- Reading and editing excel files
- Work with PDFs
- Automate emails and text messages
- Fill out forms

Python can do data science and machine learning tasks:
- Analyze large data files
- Create visualizations
- Perform machine learning tasks
- Create and run predictive algorithms

Python can create websites:
- Use web frameworks such as Django and Flask to handle the backend of a website and user data
- Create interactive dashboards for users

## Installing Python
To install Python, here we will use the free Individual Anaconda distribution - it includes Python and many other useful libraries, including Jupyter Notebook env. 

In the home page, click the Launch inside the Jupyter Notebook card. A terminal should open, in the terminal, type `jupyter-notebook` and hit Enter. After a while, it should open in browser a UI interface, which allow you to navigate the file system of the computer. Click the New button on the right, and choose Folder, it will create a new folder in the current directory. You can then create notebooks inside. Rename the folder as my-python-stuff, by select the check mark on its left, and click the Rename button. Inside this folder, click New, and choose Python 3, and it will automatically launch and connect to a new notebook. A notebook is an env with individual cells where you can write Python code. In the cell, type `1+1`, and Cell -> Run Cells. Then it will run the cell and output `2`. If we use `Shift + Enter`, then it will run current cell and create a new cell underneath it, and so on and on. Help -> User Interface Tour go get familiar with UI. 

If we close the notebook tab, we can see in main page that this notebook is green, which means it is running. If we click the checkbox on its left, and click Shutdown, it will stop running, and icon turns grey. Similarly, you can also delete it. You can also delete this folder in the same way. 

There are also many free "No Install" options to run Python code: 
- jupyter.org/try
- Google Collab Online Notebooks
- Repl.it

The drawback of the "No Install" options are, it is hard to upload your own code, data or notebooks, also, they may not save your code in the free version. 

## Running Python Code
3 main types of development environments: 
- Text editors: most are not designed with Python in mind, usually free, such as Sublime Text and Atom
- Full IDEs: designed specifically for Python, only community editions are free, pro version has a lot of extra functionality, such as PyCharm and Spyder
- Notebook environments: Great for learning, can see input and output next to each other. Support in-line markdown notes, visualizations, videos, etc. Special file formats that are .ipynb, instead of .py. Most popular is Jupyter Notebook. It is getting more and more popular with machine learning and data science. 

The example python code: 
```py
print("Hello world")
```
And save it as test.py file. To run it, use `python test.py`. 

To run code in Jupyter Notebook, you can open a XXX.py file and edit it in the browser. But is it not very convenient. The notebook system is good though. You can rename the notebook in the browser in the opened notebook page. When you create a new cell, it defaults to a Code cell, but you can click on the drop down in the UI and change it to a Markdown cell for simple text. You have to open the .ipynb files using the jupyter notebook system. 





















