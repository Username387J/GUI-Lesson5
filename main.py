from tkinter import *
import tkinter.font as font 
root = Tk()
root.geometry("500x500")
root.title("Celsius to Farenheit Converter")

titlelabel = Label(root,text="Celsius -> Farenheit",font=font.Font(size=20))
titlelabel.pack()

frame = Frame(root)
# can add padx
frame.pack(pady=20)

temperaturelabel = Label(frame,text="Enter temperature in Celsius: ")
temperaturelabel.grid(row=0,column=0)

celsiusentry = Entry(frame,width=50)
celsiusentry.grid(row=0,column=1)

errorlabel = Label(frame,text="Please enter valid input..")
#errorlabel.grid(row=1,column=1)

outputlabel = Label(frame,text="Hi")
outputlabel.grid(row=2,column=0)

converterbutton= Button(frame,text="Convert",command=None)
converterbutton.grid(row=3,column=0)





root.mainloop()
