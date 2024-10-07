from tkinter import *
from tkinter.messagebox import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
fr=Frame(root)
fr.grid(row=0,column=0,columnspan=10)
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,padx=w//2.7,columnspan=15)
Label(root,text='Online Bus Booking System',fg="red",bg="sky blue",font=('Times',24)).grid(row=1,column=4,pady=25,padx=25,columnspan=10)
fr3=Frame(root)
fr3.grid(row=2,column=4)
Label(fr3,text="Bus Ticket",font=('arial',15,'bold'),fg="green",bg="light green").grid(padx=w//3)
fr4=Frame(root)
fr4.grid(row=4,column=4)
text_box=Text(fr4,font=('arial',10),bg="light blue")
text_box.grid(pady=10)
showinfo("SEAT BOOKING","SEAT BOOKED")

def close():
    if askyesnocancel("Quit","for closing click YES \n click NO for mainmenu"):
        showinfo("INFO","THANKYOU FOR USING PYTHON BUS SERVICES")
        root.destroy()
root.protocol("WM_DELETE_WINDOW",close)
root.mainloop()
