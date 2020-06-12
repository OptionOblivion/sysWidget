from tkinter import *

gui = Tk()
gui.title("PowerBoi 9000")
gui.geometry("300x400")
gui.resizable(0,0)
gui.configure(bg="white")

label_life = Label(gui, text='Percentage:',fg="black", bg="white",font="none 16 bold underline").grid(row=0,column=0,  sticky=W)
label_percentage= Label(gui, text='N/A', fg="red", font="none 16 bold").grid(row=0,column=1, sticky=W)
label_time = Label(gui, text='Time Remaining:',fg="black", bg="white",font="none 16 bold underline").grid(row=1,column=0)

label_hours = Label(gui, text='N/A', fg="red", font="none 16 bold").grid(row=1,column=1)


gui.mainloop()
