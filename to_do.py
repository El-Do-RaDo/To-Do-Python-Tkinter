#importing the required libraries
import tkinter as tk
from tkinter import messagebox

#creating the window/GUI
win = tk.Tk()

#creating label
label_1 = tk.Label(win, text="To-Do List")
label_1.grid(row=0,column=0)

#creating a text field
txt_inp = tk.Entry(win)
txt_inp.grid(row=1,column=1)

#creating the buttons
button_1 = tk.Button(win,text="Add Task",fg="black",command=add_task,width="7")
button_1.grid(row=1,column=0)

button_2 = tk.Button(win,text="Edit",fg="black",command=edit,width="7")
button_2.grid(row=2,column=0)

button_3 = tk.Button(win,text="Delete",fg="black",command=delete,width="7")
button_3.grid(row=3,column=0)

button_4 = tk.Button(win,text="Delete All",fg="black",command=delete_all,width="7")
button_4.grid(row=4,column=0)

button_5 = tk.Button(win,text="Exit",fg="black",command=quit,width="7")
button_5.grid(row=5,column=0)

#creating the list_box
list_tsk = tk.Listbox(win)
list_tsk.grid(row=2,column=1,rowspan=5)



win.mainloop()