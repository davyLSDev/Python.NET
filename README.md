# Python.NET

## About
Finding a crossplatform gui toolkit that works for C# / .NET project is challenging. A traditional approach was to use "winforms", but this not only looks rather ugly and dated, it doesn't work very well for *nix variants, such as Linux, or OSX. There are two well-known crossplatform gui toolkits for c++, namely: wxWidgets, and Qt. In thinking about what could bridge such toolkits the idea of possibly looking into using Python as there exist bindings for Python and either of these two toolkits. Then, the challenge was to see if there were any bindings for .NET, and lo and behold there are. That is where this experiment started to take shape.

This repo itslef, came about as a result of some experimentation with Python .NET, and few other libraries such as Qt, and wx. The second commit is simply a copy of the work that was already done but not committed to any particular repository. The work that was done was hastily put together by shamelessly copying the work of others and combining it to make two very simple applications, one using Qt, and the other, for wxWidgets.

## Getting set up

1. Need the following packages:
* pythonnet - Integrate Python with .NET Common Language Runtime, aka clr

* wxPython - Python wx bindings
* wxGlade - graphical gui building tool for wx (other options ... wxformbuilder - builds guis for python3) 
* PyQt4 - Python Qt binding packages
* (PySide4, PyQt5 - other Python Qt binding package alternatives not used in this repo)

2. Install needed packages:
```
pip install pythonnet
pip install wxPython 
sudo apt-get install python-qt4
sudo apt-get install wxglade
```

3. make a dll library 
The math dll library was created with the ff command:

```
csc /t:library MyMath.cs
```
## Tutorials

[Python.NET](code-maven.com/slides/python/python-and-dotnet)
[PyQt4](https://zetcode.com/gui/pyqt4/)
[wxPython](https://zetcode.com/wxpython/)


