from tkinter import *

gui = Tk()
gui.title("PowerBoi 9000")
gui.geometry("300x400")
gui.resizable(0,0)
gui.configure(bg="royalblue")

label_life = Label(gui,  text='Battery Life: ',fg="black", font="none 16 bold").grid(row=1,column=0)
label_percentage= Label(gui, text='insert data here', fg="red", font="none 16 bold").grid(row=1,column=1)


gui.mainloop()
