from tkinter import *

class GUI:

    def __init__(self):
        pass

    gui = Tk()
    gui.title("PowerBoi 9000")
    gui.geometry("300x400")
    gui.resizable(0,0)
    icon = PhotoImage(file="icon.png")
    gui.iconphoto(False, icon)

    label_life = Label(gui, text='Percentage:', fg="black", bg="white", font="none 16 bold underline").grid(row=0,column=0,sticky=W)
    label_percentage = Label(gui, text='N/A', fg="red", font="none 16 bold").grid(row=0, column=1, sticky=W)
    label_time = Label(gui, text='Time Remaining:', fg="black", bg="white", font="none 16 bold underline").grid(row=1,column=0)
    label_hours = Label(gui, text='N/A', fg="red", font="none 16 bold").grid(row=1, column=1)
    colorChange = Button(gui, text='Dark', activebackground="royalblue" ).grid(row=3, column=0)
    colorChange = Button(gui, text='Light', activebackground="royalblue").grid(row=3, column=1)
    gui.mainloop()

class Battery:

    def __init__(self):
        percentage=0;
        time=0;

    def get_percentage(self):
        pass
        #will return percentage data

    def get_time(self):
        pass
        #will return time remaining data
