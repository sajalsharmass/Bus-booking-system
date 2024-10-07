from tkinter import *
from tkinter.messagebox import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='.\\Bus_for_project.png')

Label(root,image=img).grid(row=0,column=1,columnspan=12,padx=w//2.7)
Label(root,text='Online Bus Booking System',fg="red",bg="sky blue",font=('Times',24)).grid(row=1,column=3,columnspan=9,pady=25)

Button(root,text="Seat Booking",bg="red",fg="black",font=('Arial',12)).grid(row=2,column=5,padx=10)
Button(root,text="Checked Booked Seats",bg="yellow",font=('Arial',12)).grid(row=2,column=6,padx=10)
Button(root,text="Add Bus Details",bg="light green",font=('Arial',12)).grid(row=2,column=7)

Label(root,text="For Admin Only",fg="red").grid(row=3,column=7,pady=10)
root.mainloop()
  
