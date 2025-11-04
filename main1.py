from tkinter import *
import tkinter.font as font
root = Tk()
root.geometry("400x400")
root.title("Weight Converter")

def change():
    kg=kgentry.get()
    if(kg.replace(".","").isnumeric()):
        warninglabel.grid_forget()
        pound=round((float(kg)*2.3),2)
        outputlabel.config(text="The weight in pounds is approximately: "+str(pound))
    else:
        warninglabel.grid(row=2,column=0)



titlelabel=Label(root,text="KG to Pound Converter",font=font.Font(size=20))
titlelabel.pack()

frame = Frame(root)
frame.pack(pady=20)

kglabel=Label(frame,text="Enter KG Here: ")
kglabel.grid(row=0,column=0)

kgentry=Entry(frame,width=67)
kgentry.grid(row=1,column=0)

warninglabel =Label(frame,text="Please input numbers only! ")
#warninglabel.grid(row=2,column=0)

outputlabel = Label(frame)
outputlabel.grid(row=3,column=0)

convertbutton = Button(frame,text="Convert",command=change)
convertbutton.grid(row=4,column=0)




root.mainloop()