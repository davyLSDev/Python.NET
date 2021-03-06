#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0 on Thu Mar 25 15:49:05 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((800, 300))
        self.spin_ctrl_1 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_2 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Calculator Form")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        grid_sizer_1 = wx.GridSizer(0, 7, 3, 1)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Input 1")
        grid_sizer_1.Add(label_1, 0, wx.ALL, 7)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Input 2")
        grid_sizer_1.Add(label_2, 0, wx.ALL, 7)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Output")
        grid_sizer_1.Add(label_3, 0, wx.ALL, 7)
        grid_sizer_1.Add(self.spin_ctrl_1, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "+")
        grid_sizer_1.Add(label_4, 0, wx.ALL, 7)
        grid_sizer_1.Add(self.spin_ctrl_2, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, "=")
        grid_sizer_1.Add(label_5, 0, wx.ALL, 7)
        grid_sizer_1.Add(self.text_ctrl_1, 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.Calculator_Form = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.Calculator_Form)
        self.Calculator_Form.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
