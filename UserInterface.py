#!/usr/bin/env python
# coding:utf-8

import wx
from FileSearching import FileSearching
from ImgIntegrating import ImageHandler


class UserInterface(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, -1, u"图片合成", size=(500, 500))

        self.panel = wx.Panel(self, -1)
    #     self.initWidgets(self.panel)
    #
    # def initWidgets(self, panel):
        sizer = wx.GridBagSizer(0, 0)

        label_no1 = wx.StaticText(self.panel, -1, u"第1张图片关键字：")
        sizer.Add(label_no1, pos=(1, 0), flag=wx.ALL, border=5)
        self.text_no1 = wx.TextCtrl(self.panel, -1, "bgh", size=(175, -1))
        sizer.Add(self.text_no1, pos=(1, 1), flag=wx.ALL, border=5)

        label_no2 = wx.StaticText(self.panel, -1, u"第2张图片关键字：")
        sizer.Add(label_no2, pos=(2, 0), flag=wx.ALL, border=5)
        self.text_no2 = wx.TextCtrl(self.panel, -1, "sfz_f", size=(175, -1))
        sizer.Add(self.text_no2, pos=(2, 1), flag=wx.ALL, border=5)

        label_no3 = wx.StaticText(self.panel, -1, u"第3张图片关键字：")
        sizer.Add(label_no3, pos=(3, 0), flag=wx.ALL, border=5)
        self.text_no3 = wx.TextCtrl(self.panel, -1, "sfz_b", size=(175, -1))
        sizer.Add(self.text_no3, pos=(3, 1), flag=wx.ALL, border=5)

        label_no4 = wx.StaticText(self.panel, -1, u"第4张图片关键字：")
        sizer.Add(label_no4, pos=(4, 0), flag=wx.ALL, border=5)
        self.text_no4 = wx.TextCtrl(self.panel, -1, "ddh", size=(175, -1))
        sizer.Add(self.text_no4, pos=(4, 1), flag=wx.ALL, border=5)

        label_file_button = wx.StaticText(self.panel, -1, u"选择图片文件夹：")
        sizer.Add(label_file_button, pos=(5, 0), flag=wx.ALL, border=5)
        file_button = wx.Button(self, -1, u"文件夹选择")
        self.Bind(wx.EVT_BUTTON, self.on_file_choose_button, file_button)
        sizer.Add(file_button, pos=(5, 1), flag=wx.ALL, border=5)

        label_dir = wx.StaticText(self.panel, -1, u"文件夹路径：")
        sizer.Add(label_dir, pos=(6, 0), flag=wx.ALL, border=5)
        self.label_dir_output = wx.StaticText(self.panel, -1, "..................................................................................")
        self.label_dir_output.Hide()
        sizer.Add(self.label_dir_output, pos=(6, 1), flag=wx.FULLSCREEN_ALL, border=5)

        self.label_image_group_number_all = wx.StaticText(self.panel, -1)
        sizer.Add(self.label_image_group_number_all, pos=(7, 0), flag=wx.ALIGN_CENTER, border=5)
        self.label_image_group_number_integrated = wx.StaticText(self.panel, -1)
        sizer.Add(self.label_image_group_number_integrated, pos=(7, 1), flag=wx.ALIGN_CENTER, border=5)

        self.integrate_button = wx.Button(self, -1, u"开始合成")
        self.Bind(wx.EVT_BUTTON, self.on_integrate_button, self.integrate_button)
        sizer.Add(self.integrate_button, pos=(9, 1), flag=wx.ALL, border=5)

        self.panel.SetSizerAndFit(sizer)
        self.Show()

    # ----------------------------------------------------------------------
    def on_file_choose_button(self, event):
        """"""
        dlg = wx.DirDialog(self, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            dir_path = dlg.GetPath()  # file path
            self.label_dir_output.Show()
            self.label_dir_output.SetLabel(dir_path)

        dlg.Destroy()

    def set_img_group_number_all(self, number_all):
        self.label_image_group_number_all.SetLabel(u"图片组数量："+ str(number_all))

    def set_img_group_number_integrated(self, number_integrated):
        self.label_image_group_number_integrated.SetLabel(u"已处理图片组数量："+ str(number_integrated))

    # def get_dir_path(self):
    #     dir_path = str(self.label_dir_output.GetLabel())
    #     return dir_path

###############################################################################
    def on_integrate_button(self, event):
        '''-----------------------integrating starts---------------------'''


        print "Clicking on Integrating Button...."
        target_file_path = self.label_dir_output.GetLabel()
        print target_file_path
        file_handle = FileSearching(target_file_path)
        print file_handle.getFileNumber()
        print file_handle.calculateTransactionNumber("0011111", ".jpg")

        image_file_list = ["bgh", "sfz_f", "sfz_b", "ddh"]
        tempImages = ["0011111_bgh.jpg", "0011111_sfz_f.jpg", "0011111_sfz_b.jpg", "0011111_ddh.jpg"]
        output_path = "/Users/ryan/Documents/ImgIntegration"
        output_name = "0011111_final.jpg"

        image_handle = ImageHandler(image_file_list)
        image_handle.init_image_type_dict()
        print image_handle.image_integrating(target_file_path, tempImages, output_path, output_name, None, None)
