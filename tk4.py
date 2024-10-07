from tkinter import *
from tkinter.messagebox import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,padx=w//3,columnspan=15)
Label(root,text='Online Bus Booking System',fg="red",bg="sky blue",font=('Times',24)).grid(row=1,column=4,pady=25,padx=25,columnspan=10)

Button(root,text="New Bus",bg="light green").grid(row=3,column=7)
Button(root,text="New Operator",bg="orange").grid(row=3,column=8)
Button(root,text="New Route",bg="blue").grid(row=3,column=9)
Button(root,text="New Run",bg="light pink").grid(row=3,column=10)
root.mainloop()
