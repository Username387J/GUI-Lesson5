from tkinter import *
import tkinter.font as font
root=Tk()
root.geometry("500x500")
root.title("Currency Converter")

def change():
    USD=USDentry.get()
    if(USD.replace(".","").isnumeric()):
        noticelabel.grid_forget()
        CAD=round((float(USD)*1.41),3)
        outputlabel.config(text="The amounr in CAD as of now is approximately: ﹩"+str(CAD))
    else:
        noticelabel.grid(row=2,column=0)




titlelabel=Label(root,text="USD to CAD ",font=font.Font(size=20))
titlelabel.pack()

frame=Frame(root)
frame.pack(pady=20)

USDlabel=Label(frame,text="Enter USD here: ")
USDlabel.grid(row=1,column=0)

USDentry=Entry(frame,width=41)
USDentry.grid(row=2,column=0)

noticelabel = Label(frame,text="Please enter a number")


outputlabel = Label(frame)
outputlabel.grid(row=3,column=0)

converterbutton= Button(frame,text="Convert",command=change)
converterbutton.grid(row=4,column=0)




root.mainloop()
