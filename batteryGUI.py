from tkinter import *
gui = Tk()
gui.configure(bg='white')
gui.title("PowerBoi 9000")
gui.geometry("300x400")
gui.resizable(0, 0)
icon = PhotoImage(file="icon.png")
gui.iconphoto(False, icon)

label_life = Label(gui, text='Percentage:', fg="black", bg="white", font="none 16 bold underline").grid(row=0,column=0, sticky=W)
label_percentage = Label(gui, text='N/A', fg="red", font="none 16 bold").grid(row=0, column=1, sticky=E)
label_time = Label(gui, text='Time Remaining:', fg="black", bg="white", font="none 16 bold underline").grid(row=1,column=0,sticky=W)
label_hours = Label(gui, text='N/A', fg="red", font="none 16 bold").grid(row=1, column=1, sticky=E)
label_filler = Label(gui, bg='white').grid(row=2, column=0, pady=140)

def filler():
    filler=Label(gui, bg='dimgrey').grid(row=2, column=0, pady=140)

def filler_wht():
    fillWhite=Label(gui, bg='white').grid(row=2, column=0, pady=140)

but_dark = Button(gui, text='Dark', command=lambda:[gui.configure(bg='dimgrey'),filler()]).grid(row=3,column=0)
but_light = Button(gui, text='Light', command=lambda:[gui.configure(bg='white'),filler_wht()]).grid(row=3,column=1)

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
