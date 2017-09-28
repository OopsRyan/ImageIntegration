# coding=utf-8
from Tkinter import *
import tkFileDialog
import tkMessageBox
from Preprocessor import Preprocessor


class UserInterface:

    def __init__(self):

        self.root = Tk()
        self.root.title(u"Image_integrating")
        self.root.geometry('470x320')
        ########
        self.frm = Frame(self.root)
        # Top
        Label(self.root, text=" ", font=('Arial', 15)).pack()
        self.frm = Frame(self.root)
        # Left
        self.frm_L = Frame(self.frm)
        self.frm_L1 = Frame(self.frm_L)
        self.frm_L2 = Frame(self.frm_L)
        self.frm_L3 = Frame(self.frm_L)
        self.frm_L4 = Frame(self.frm_L)

        # self.var_char1 = StringVar()
        # self.var_char2 = StringVar()
        # self.var_char3 = StringVar()
        # self.var_char4 = StringVar()

        # self.var_char1.set("bgh")
        # self.var_char2.set("sfz_f")
        # self.var_char3.set("sfz_b")
        # self.var_char4.set("ddh")

        # Label(self.frm_L1, text='�������1��ͼƬ�Ĺؼ��֣�'.decode('gbk').encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        # Entry(self.frm_L1, textvariable=self.var_char1, width=15, font=('Verdana', 15)).pack(side=RIGHT)
        # self.frm_L1.pack()
        # Label(self.frm_L2, text='�������2��ͼƬ�Ĺؼ��֣�'.decode('gbk').encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        # Entry(self.frm_L2, textvariable=self.var_char2, width=15, font=('Verdana', 15)).pack(side=RIGHT)
        # self.frm_L2.pack()
        # Label(self.frm_L3, text='�������3��ͼƬ�Ĺؼ��֣�'.decode('gbk').encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        # Entry(self.frm_L3, textvariable=self.var_char3, width=15, font=('Verdana', 15)).pack(side=RIGHT)
        # self.frm_L3.pack()
        # Label(self.frm_L4, text='�������4��ͼƬ�Ĺؼ��֣�'.decode('gbk').encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        # Entry(self.frm_L4, textvariable=self.var_char4, width=15, font=('Verdana', 15)).pack(side=RIGHT)
        # self.frm_L4.pack()

        self.frm_L.pack(side=TOP)

        # Middle
        self.frm_M = Frame(self.frm)
        self.frm_M1 = Frame(self.frm_M)
        self.frm_M2 = Frame(self.frm_M)
        self.frm_M3 = Frame(self.frm_M)
        self.frm_M4 = Frame(self.frm_M)
        self.frm_M5 = Frame(self.frm_M)
        self.frm_M6 = Frame(self.frm_M)

        Label(self.frm_M5, text=u'csv path:', font=('Arial', 12)).pack(side=LEFT)
        self.csv_input_path = StringVar()
        Label(self.frm_M5, textvariable=self.csv_input_path, font=('Arial', 12)).pack(side=RIGHT)
        self.frm_M5.pack()

        Button(self.frm_M6, text=u"choose", command=self.csv_input_button_click, width=15, height=2,
               font=('Arial', 10)).pack(side=LEFT)
        self.frm_M6.pack()

        Label(self.frm_M1, text=u'image path:', font=('Arial', 12)).pack(side=LEFT)
        self.text_input_path = StringVar()
        Label(self.frm_M1, textvariable=self.text_input_path, font=('Arial', 12)).pack(side=RIGHT)
        self.frm_M1.pack()

        Button(self.frm_M2, text=u"choose", command=self.input_button_click, width=15, height=2,
               font=('Arial', 10)).pack(side=LEFT)
        self.frm_M2.pack()

        Label(self.frm_M3, text=u'output path:', font=('Arial', 12)).pack(side=LEFT)
        self.text_output_path = StringVar()
        Label(self.frm_M3, textvariable=self.text_output_path, font=('Arial', 12)).pack(side=RIGHT)
        self.frm_M3.pack()

        Button(self.frm_M4, text=u"choose", command=self.output_button_click, width=15, height=2,
               font=('Arial', 10)).pack(side=LEFT)
        self.frm_M4.pack()

        self.frm_M.pack()

        # Bottom
        self.frm_B = Frame(self.frm)
        self.frm_BT = Frame(self.frm_B)

        self.img_group_number = StringVar()
        Label(self.frm_B, textvariable=self.img_group_number, font=('Arial', 15)).pack(side=TOP)
        Button(self.frm_BT, text="start".decode('gbk').encode('utf-8'), command=self.integrate_images, width=10, height=2,
               font=('Arial', 15)).pack(side=BOTTOM)
        self.frm_BT.pack(side=TOP)

        self.t_show = Text(self.frm_B, width=20, height=5, font=('Verdana', 15))
        self.t_show.pack()

        self.frm_B.pack(side=BOTTOM)

        self.frm.pack()
        ########

    def csv_input_button_click(self):
        filename = tkFileDialog.askopenfile()
        print filename
        self.csv_input_path.set(filename)

    def input_button_click(self):
        filename = tkFileDialog.askdirectory()
        self.text_input_path.set(filename)

    def output_button_click(self):
        filename = tkFileDialog.askdirectory()
        self.text_output_path.set(filename)

    def judge_user_input_or_not(self):
        alert_message = StringVar()
        # if len(self.var_char1.get()) == 0 or len(self.var_char2.get()) == 0 \
        #         or len(self.var_char3.get()) == 0 or len(self.var_char4.get()) == 0:
        #     alert_message.set(u"������ͼƬ�ؼ���!\n")

        if len(self.text_input_path.get()) == 0:
            alert_message.set(alert_message.get() + u"input path is empty!\n")

        if len(self.text_output_path.get()) == 0:
            alert_message.set(alert_message.get() + u"output path is empty!\n")

        if len(alert_message.get()):
            tkMessageBox.showwarning(u"warning", alert_message.get())

    def integrate_images(self):

        self.judge_user_input_or_not()

        image_type_list = list()
        # image_type_list.append(self.var_char1.get())
        # image_type_list.append(self.var_char2.get())
        # image_type_list.append(self.var_char3.get())
        # image_type_list.append(self.var_char4.get())

        integrate_handler = Preprocessor(self.text_input_path.get(), self.text_output_path.get(),
                                         image_type_list)

        group_number = integrate_handler.get_group_number_all()
        self.img_group_number.set(u"Total number: "+str(group_number)+u" groups")
        integrated_number = 0

        keyword_dict = integrate_handler.get_keyword_dict()
        for k, v in keyword_dict.iteritems():
            if integrate_handler.integrate_images(k):
                integrated_number += 1
                self.t_show.insert(END, u"No. "+str(integrated_number)+u" has been finished!\n")


if __name__ == "__main__":
    d = UserInterface()
    mainloop()

