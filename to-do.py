from tkinter import *
import tkinter.messagebox 
love = Tk()
love.geometry("654x354")
love.title("To-Do GUI Application")
love.maxsize(600,400)
love.minsize(560,340)

def printInput(): 
	inp = inputtxt.get(1.0, "end-1c") 
	lbl.config(text = " "+inp) 
     
def peace(event):
    print(f"You clicked on the button at {event.x},{event.y}")
def update():
    tkinter.messagebox.showinfo("TO-DO IS HAPPY NOW",  f"Hi,{namevalueentry.get()}your tasks are updated")
Label(love, text="Welcome to To-Do manager.\nYou can manage your activities here.", bg="skyblue",fg="black",padx=13,pady=4).grid(row=0,column=3)

name= Label(love, text="Your Name:")
date = Label(love, text="Today's Date:")
name.grid(row=0,column=5)
date.grid(row=1,column=5)
namevalue = StringVar()
datevalue = StringVar()
namevalueentry = Entry(love, textvariable=namevalue)
datevalueentry = Entry(love, textvariable=datevalue)
namevalueentry.grid(row=0,column=6)
datevalueentry.grid(row=1,column=6)
widget = Button(love, text="Click to update",padx=2,pady=5,bg="lightgreen",command=update)
widget.grid(row=4,column=6)
widget.bind('<Button-1>', peace)


inputtxt = Text(love, 
				height = 14, 
				width = 20, bg="LIGHTPINK",relief=RIDGE) 
inputtxt.grid(row=2,column=3)

newtxt = Listbox(love,
              height=10, width=19,bg='lightyellow',relief=GROOVE)
newtxt.grid(row=2,column=6)
printButton = Button(love, 
						text = "update", 
						command = printInput)
printButton.grid(row=4,column=3)
submit = Button
lbl = Label(love,text="", relief=SUNKEN) 
lbl.grid(row=2,column=6,padx=5,pady=15) 


love.mainloop()
