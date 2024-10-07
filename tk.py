from tkinter import *
from tkinter.messagebox import *
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='.\\Bus_for_project.png')

Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=w//2.7)
Label(root,text='Online Bus Booking System',fg="red",bg="sky blue",font=('Times',24)).grid(row=1,column=3,columnspan=3,pady=20)
Label(root,text="Enter your name",fg="blue",font=('Arial',15,'bold')).grid(row=2,column=3,pady=10)
Label(root,text="Sajal Sharma",fg="blue",font=('Arial',13)).grid(row=2,column=4)

Label(root,text="Er No.",fg="blue",font=('Arial',15,'bold')).grid(row=3,column=3,pady=10)
Label(root,text="211B264",fg="blue",font=('Arial',13)).grid(row=3,column=4)

Label(root,text="Mobile",fg="blue",font=('Arial',15,'bold')).grid(row=4,column=3,pady=10)
Label(root,text="9770872928",fg="blue",font=('Arial',13)).grid(row=4,column=4)

Label(root,text="Submitted To: Dr.Mahesh Kumar",fg="red",bg="sky blue",font=('Times',12)).grid(row=5,column=4,pady=20)
Label(root,text="Project Based Learning",fg="red",bg="sky blue",font=('Times',12)).grid(row=6,column=4)
root.mainloop()
