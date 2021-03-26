#!/usr/bin/env python
# Modified for using the dot net dll

"""
ZetCode wxPython tutorial

This example shows a simple
message box.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

# This stuff is for the dot net dll import
import clr
dll = clr.FindAssembly('MyMath')  # returns path to dll
assembly = clr.AddReference('MyMath')
#print(type(assembly)) # <class 'System.Reflection.RuntimeAssembly'>
#print(dir(assembly))
from MyMath import MyMathClass
from MyMath import MyMathClass as My

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        wx.CallLater(3000, self.ShowMessage)

        self.SetSize((300, 200))
        self.SetTitle('Message box')
        self.Centre()

    def ShowMessage(self):
        wx.MessageBox('Use dot net dll math library to add 3 and 4 to get =>'+ str(My.addInts(3, 4)), 'Info',
            wx.OK | wx.ICON_INFORMATION)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
