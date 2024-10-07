from tkinter import *
from tkinter.messagebox import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=w//3,columnspan=15)
Label(root,text='Online Bus Booking System',fg="red",bg="sky blue",font=('Times',24)).grid(row=1,column=3,pady=25,padx=25,columnspan=10)
Label(root,text="Check Your Booking",font=("Arial",12),bg="light green").grid(row=2,column=7,pady=15)
Label(root,text="Enter your Mobile No:").grid(row=3,column=6)
Entry(root).grid(row=3,column=7)
Button(root,text="Check Booking").grid(row=3,column=8)
root.mainloop()
