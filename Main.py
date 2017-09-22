# coding: utf-8
import os
import sys
import wx
from FileSearching import FileSearching
from ImgIntegrating import ImageHandler
from UserInterface import UserInterface

if __name__ == '__main__':
    frame = wx.App()
    app = UserInterface()
    frame.MainLoop()

