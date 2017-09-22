# -*- coding:cp936 -*-
from Tkinter import *
import tkFileDialog
import tkMessageBox

class show:
    num_info_hash = {}
    char_info_hash = {}
    num_char = {}
    char_num = {}

    def __init__(self):

        self.root = Tk()
        self.root.title("图片合成".decode('gbk').encode('utf8'))
        # self.root.geometry('470x320')
        ########
        self.frm = Frame(self.root)
        # Top
        Label(self.root, text="图片合成".decode('gbk').encode('utf8'), font=('Arial', 15)).pack()
        self.frm = Frame(self.root)
        # Left
        self.frm_L = Frame(self.frm)
        self.frm_L1 = Frame(self.frm_L)
        self.frm_L2 = Frame(self.frm_L)
        self.frm_L3 = Frame(self.frm_L)
        self.frm_L4 = Frame(self.frm_L)

        self.var_char1 = StringVar()
        self.var_char2 = StringVar()
        self.var_char3 = StringVar()
        self.var_char4 = StringVar()

        self.var_char1.set("bgh")
        self.var_char2.set("sfz_f")
        self.var_char3.set("sfz_b")
        self.var_char4.set("ddh")

        Label(self.frm_L1, text='请输入第1张图片的关键字：'.decode('gbk').encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        Entry(self.frm_L1, textvariable=self.var_char1, width=15, font=('Verdana', 15)).pack(side=RIGHT)
        self.frm_L1.pack()
        Label(self.frm_L2, text='请输入第2张图片的关键字：'.decode('gbk').encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        Entry(self.frm_L2, textvariable=self.var_char2, width=15, font=('Verdana', 15)).pack(side=RIGHT)
        self.frm_L2.pack()
        Label(self.frm_L3, text='请输入第3张图片的关键字：'.decode('gbk').encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        Entry(self.frm_L3, textvariable=self.var_char3, width=15, font=('Verdana', 15)).pack(side=RIGHT)
        self.frm_L3.pack()
        Label(self.frm_L4, text='请输入第4张图片的关键字：'.decode('gbk').encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        Entry(self.frm_L4, textvariable=self.var_char4, width=15, font=('Verdana', 15)).pack(side=RIGHT)
        self.frm_L4.pack()

        self.frm_L.pack(side=TOP)

        # Middle
        self.frm_M = Frame(self.frm)
        self.frm_M1 = Frame(self.frm_M)
        self.frm_M2 = Frame(self.frm_M)
        self.frm_M3 = Frame(self.frm_M)
        self.frm_M4 = Frame(self.frm_M)

        Label(self.frm_M1, text='输入路径:'.decode('gbk').encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        self.text_input_path = StringVar()
        Label(self.frm_M1, textvariable=self.text_input_path, font=('Arial', 12)).pack(side=RIGHT)
        self.frm_M1.pack()

        Button(self.frm_M2, text="选择".decode('gbk').encode('utf-8'), command=self.input_button_click, width=15, height=3,
               font=('Arial', 10)).pack(side=LEFT)
        self.frm_M2.pack()

        Label(self.frm_M3, text='输出路径:'.decode('gbk').encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        self.text_output_path = StringVar()
        Label(self.frm_M3, textvariable=self.text_output_path, font=('Arial', 12)).pack(side=RIGHT)
        self.frm_M3.pack()

        Button(self.frm_M4, text="选择".decode('gbk').encode('utf-8'), command=self.output_button_click, width=15, height=3,
               font=('Arial', 10)).pack(side=LEFT)
        self.frm_M4.pack()

        self.frm_M.pack()

        # Bottom
        self.frm_B = Frame(self.frm)
        self.frm_BT = Frame(self.frm_B)

        self.img_group_number = StringVar()
        Label(self.frm_B, textvariable=self.img_group_number, font=('Arial', 15)).pack(side=TOP)
        Button(self.frm_BT, text="开始合成".decode('gbk').encode('utf-8'), command=self.integrate_images, width=10, height=3,
               font=('Arial', 15)).pack(side=BOTTOM)
        self.frm_BT.pack(side=TOP)

        self.t_show = Text(self.frm_B, width=20, height=5, font=('Verdana', 15))
        self.t_show.insert('1.0', '')
        self.t_show.pack()

        self.frm_B.pack(side=BOTTOM)

        self.frm.pack()
        ########

    def input_button_click(self):
        filename = tkFileDialog.askdirectory()
        print filename
        self.text_input_path.set(filename)

    def output_button_click(self):
        filename = tkFileDialog.askdirectory()
        self.text_output_path.set(filename)

    def integrate_images(self):
        self.img_group_number.set("click on integrate_button")
        self.judge_user_input_or_not()

    def judge_user_input_or_not(self):
        alert_message = StringVar()
        if len(self.var_char1.get()) == 0 or len(self.var_char2.get()) == 0 \
                or len(self.var_char3.get()) == 0 or len(self.var_char4.get()) == 0:
            alert_message.set(u"请输入图片关键字!\n")

        if len(self.text_input_path.get()) == 0:
            alert_message.set(alert_message.get() + u"请选择图片输入路径!\n")

        if len(self.text_output_path.get()) == 0:
            alert_message.set(alert_message.get() + u"请选择图片输出路径!\n")

        if len(alert_message.get()):
            tkMessageBox.showwarning(u"警告", alert_message.get())


if __name__ == "__main__":
    d = show()
    mainloop()