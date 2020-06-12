from tkinter import *
import threading
from sysinfo import *


class SysinfoThread():

    def __init__(self):
        super().__init__(self)
        self.widgetMap = {}  # will be dictionary that maps a information to given tkinter widget.
        # key is the information, value is widget

    def update_widgets(self):
        for k, v in self.widgetMap:
            pass


class BatteryGUI():
    """Class that contains the GUI. Possible problem is the extra thread will make this class be a global var, which breaks OOP """

    def __init__(self):
        self.gui = Tk()
        self.gui.configure(bg='white')
        self.gui.title("PowerBoi 9000")
        self.gui.geometry("300x400")
        self.gui.resizable(0, 0)
        self.icon = PhotoImage(file="icon.png")
        self.gui.iconphoto(False, self.icon)

        # battery percentage widget
        self.label_life = Label(self.gui, text='Percentage:', fg="black", font="none 16 bold underline").grid(row=0,column=0,pady=15, sticky=W)
        self.label_percentage = Label(self.gui, text='N/A', fg="red", font="none 16 bold").grid(row=0, column=1,sticky=E)
        #Time Remaining Widget
        self.label_time = Label(self.gui, text='Time Remaining: ', fg="black", bg="white",font="none 16 bold underline").grid(row=1, column=0, pady=15,sticky=W)
        self.label_hours = Label(self.gui, text='N/A', fg="red", font="none 16 bold").grid(row=1, column=1, sticky=E)
        #CPU Widget
        self.label_cpu=Label(self.gui, text='CPU: ', fg='black', font="none 16 bold underline").grid(row=2, column=0, pady=15, sticky=W)
        self.label_cpu_data=Label(self.gui, text='N/A', fg='red', font="none 16 bold").grid(row=2, column=1, sticky=E)
        #RAM Widget
        self.label_ram=Label(self.gui, text='RAM: ', fg='black', font='non 16 bold underline').grid(row=3, column=0, pady=15, sticky=W)
        self.label_ram_data=Label(self.gui, text='N/A', fg='red', font='none 16 bold').grid(row=3, column=1, sticky=E)
        #GPU Widget
        self.label_gpu = Label(self.gui, text='GPU: ', fg='black', font='non 16 bold underline').grid(row=3, column=0,pady=15, sticky=W)
        self.label_gpu_data = Label(self.gui, text='N/A', fg='red', font='none 16 bold').grid(row=3, column=1, sticky=E)
        #spacer
        #self.label_filler = Label(self.gui, bg='white').grid(row=2, column=0, pady=0)
        #Light Mode/Dark Mode Buttons(not definititive)
        #self.but_dark = Button(self.gui, text='Dark',command=lambda: [self.gui.configure(bg='dimgrey'), self.darkMode()]).grid(row=3,column=0)
        #self.but_light = Button(self.gui, text='Light',command=lambda: [self.gui.configure(bg='white'), self.filler_wht()]).grid(row=3,column=1)

    #def darkMode(self):
        #self.filler = Label(self.gui, bg='dimgrey').grid(row=2, column=0, pady=140)
        #self.percent_dark = Label(self.gui, text='Percentage:', fg='white', bg='dimgrey',
                                  #font="none 16 bold underline").grid(row=0, column=0, sticky=W)
       # self.time_dark = Label(self.gui, text='Time Remaining:', fg="white", bg="dimgrey",
                               #font="none 16 bold underline").grid(row=1, column=0, sticky=W)

    #def filler_wht(self):
        #self.fillWhite = Label(self.gui, bg='white').grid(row=2, column=0, pady=140)
       # self.percent_light = Label(self.gui, text='Percentage:', fg='black', bg='white',
                                  # font="none 16 bold underline").grid(row=0, column=0, sticky=W)
        #self.time_light = Label(self.gui, text='Time Remaining:', fg="black", bg="white",
                               # font="none 16 bold underline").grid(row=1, column=0, sticky=W)

    def run(self):
        self.gui.mainloop()


if __name__ == '__main__':
    GU = BatteryGUI()
    GU.run()


class Battery:

    def __init__(self):
        percentage = 0;
        time = 0;

    def get_percentage(self):
        pass
        # will return percentage data

    def get_time(self):
        pass
        # will return time remaining data
