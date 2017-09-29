# coding=utf-8
from Tkinter import *
import tkFileDialog
import tkMessageBox
from Preprocessor import Preprocessor
from CSVParser import CSVParser

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
        self.image_input_path = StringVar()
        Label(self.frm_M1, textvariable=self.image_input_path, font=('Arial', 12)).pack(side=RIGHT)
        self.frm_M1.pack()

        Button(self.frm_M2, text=u"choose", command=self.image_input_button_click, width=15, height=2,
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
        Button(self.frm_BT, text="start", command=self.integrate_images, width=10, height=2,
               font=('Arial', 15)).pack(side=BOTTOM)
        self.frm_BT.pack(side=TOP)

        self.t_show = Text(self.frm_B, width=45, height=5, font=('Verdana', 15))
        self.t_show.pack()

        self.frm_B.pack(side=BOTTOM)

        self.frm.pack()
        ########

    def csv_input_button_click(self):
        file_path = tkFileDialog.askopenfilename()
        self.csv_input_path.set(file_path)

    def image_input_button_click(self):
        file_path = tkFileDialog.askdirectory()
        self.image_input_path.set(file_path)

    def output_button_click(self):
        file_path = tkFileDialog.askdirectory()
        self.text_output_path.set(file_path)

    def judge_user_input_or_not(self):
        alert_message = StringVar()
        # if len(self.var_char1.get()) == 0 or len(self.var_char2.get()) == 0 \
        #         or len(self.var_char3.get()) == 0 or len(self.var_char4.get()) == 0:
        #     alert_message.set(u"������ͼƬ�ؼ���!\n")

        if len(self.image_input_path.get()) == 0:
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

        csv_handler = CSVParser(self.csv_input_path.get())
        data_dict = csv_handler.get_dict_from_csv()
        integrate_handler = Preprocessor(self.image_input_path.get(), self.text_output_path.get())

        # group_number = integrate_handler.get_group_number_all()

        self.img_group_number.set(u"Total number: "+str(len(data_dict))+u" groups")

        # keyword_dict = integrate_handler.get_keyword_dict()
        for k, v in data_dict.iteritems():
            return_message = integrate_handler.integrate_images(v)
            if len(return_message) > 0:
                self.t_show.insert(END, u"Ref no. " + return_message + u" has not been finished!\n")


if __name__ == "__main__":
    d = UserInterface()
    mainloop()

