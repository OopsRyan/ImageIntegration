#!/usr/bin/env python
# coding:utf-8

import wx
from FileSearching import FileSearching
from ImgIntegrating import ImageHandler
from Preprocessor import Preprocessor

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

        label_file_in_button = wx.StaticText(self.panel, -1, u"选择图片输入文件夹：")
        sizer.Add(label_file_in_button, pos=(5, 0), flag=wx.ALL, border=5)
        file_in_button = wx.Button(self, -1, u"文件夹选择")
        self.Bind(wx.EVT_BUTTON, self.on_dir_input_button, file_in_button)
        sizer.Add(file_in_button, pos=(5, 1), flag=wx.ALL, border=5)

        label_dir_in = wx.StaticText(self.panel, -1, u"图片输入文件夹路径：")
        sizer.Add(label_dir_in, pos=(6, 0), flag=wx.ALL, border=5)
        self.label_dir_input = wx.StaticText(self.panel, -1, " ........"+("          ")*10)
        self.label_dir_input.Hide()
        sizer.Add(self.label_dir_input, pos=(6, 1), flag=wx.FULLSCREEN_ALL, border=5)

        label_file_out_button = wx.StaticText(self.panel, -1, u"选择图片输出文件夹：")
        sizer.Add(label_file_out_button, pos=(7, 0), flag=wx.ALL, border=5)
        file_out_button = wx.Button(self, -1, u"文件夹选择")
        self.Bind(wx.EVT_BUTTON, self.on_dir_output_button, file_out_button)
        sizer.Add(file_out_button, pos=(7, 1), flag=wx.ALL, border=5)

        label_dir_out = wx.StaticText(self.panel, -1, u"图片输出文件夹路径：")
        sizer.Add(label_dir_out, pos=(8, 0), flag=wx.ALL, border=5)
        self.label_dir_output = wx.StaticText(self.panel, -1, " ........"+("          ")*10)
        self.label_dir_output.Hide()
        sizer.Add(self.label_dir_output, pos=(8, 1), flag=wx.FULLSCREEN_ALL, border=5)

        self.label_image_group_number_all = wx.StaticText(self.panel, -1)
        sizer.Add(self.label_image_group_number_all, pos=(9, 0), flag=wx.ALL, border=5)
        self.label_image_group_number_integrated = wx.StaticText(self.panel, -1)
        sizer.Add(self.label_image_group_number_integrated, pos=(9, 1), flag=wx.ALL, border=5)

        self.integrate_button = wx.Button(self, -1, u"开始合成")
        self.Bind(wx.EVT_BUTTON, self.on_integrate_button, self.integrate_button)
        sizer.Add(self.integrate_button, pos=(10, 1), flag=wx.ALL, border=5)

        self.panel.SetSizerAndFit(sizer)
        self.Show()

        self.tag_input_path = False
        self.tag_output_path = False

    # ----------------------------------------------------------------------
    def on_dir_input_button(self, event):
        """"""
        dlg = wx.DirDialog(self, u"选择输入文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            dir_path = dlg.GetPath()  # file path
            self.label_dir_input.Show()
            self.label_dir_input.SetLabel(dir_path)
            self.tag_input_path = True

        dlg.Destroy()

    def on_dir_output_button(self, event):
        """"""
        dlg = wx.DirDialog(self, u"选择输出文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            dir_path = dlg.GetPath()  # file path
            self.label_dir_output.Show()
            self.label_dir_output.SetLabel(dir_path)
            self.tag_output_path = True

        dlg.Destroy()

    def set_img_group_number_all(self, number_all):
        self.label_image_group_number_all.SetLabel(u"图片组数量："+ str(number_all))

    def set_img_group_number_integrated(self, number_integrated):
        self.label_image_group_number_integrated.SetLabel(u"待处理图片组数量："+ str(number_integrated))

    # def get_dir_path(self):
    #     dir_path = str(self.label_dir_output.GetLabel())
    #     return dir_path

###############################################################################

    def judge_user_input_or_not(self):

        if self.text_no1.GetValue() is None or self.text_no2.GetValue() is None \
                or self.text_no3.GetValue() is None or self.text_no4.GetValue() is None:
            self.label_dir_input.SetLabel(u"文件关键字不能为空" + ("          ") * 5)
            self.label_dir_input.Show()

        if not self.tag_input_path:
            self.label_dir_input.SetLabel(u"请选择图片输入文件夹"+("          ")*5)
            self.label_dir_input.Show()
            return

        if not self.tag_output_path:
            self.label_dir_output.SetLabel(u"请选择图片输入文件夹"+("          ")*5)
            self.label_dir_output.Show()
            return

    def on_integrate_button(self, event):
        '''-----------------------integrating starts---------------------'''
        event.Skip()

        self.judge_user_input_or_not()

        image_type_list = list()
        image_type_list.append(self.text_no1.GetValue())
        image_type_list.append(self.text_no2.GetValue())
        image_type_list.append(self.text_no3.GetValue())
        image_type_list.append(self.text_no4.GetValue())

        print image_type_list
        integrate_handler = Preprocessor(self.label_dir_input.GetLabel(), self.label_dir_output.GetLabel(),
                                         image_type_list)

        group_number = integrate_handler.get_group_number_all()
        integrated_number = 0
        self.set_img_group_number_all(group_number)

        keyword_dict = integrate_handler.get_keyword_dict()
        for k, v in keyword_dict.iteritems():
            if integrate_handler.integrate_images(k):
                integrated_number = integrated_number + 1
                self.set_img_group_number_integrated(group_number - integrated_number)



