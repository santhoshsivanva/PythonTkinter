import tkinter

#This screen dedicated for the GUI
window = tkinter.Tk()
window.title("Type Printer")
window.minsize(width=500,height=300)

#label

#label is the class you know so mylabel is the object
mylabel = tkinter.Label(background="lightyellow",text = "I am a label",font=("Arial",24,"italic"))
mylabel.pack(side = "top",expand=1)

#after creating the label you need to do the centering the pak
#default side = top
#expand
#fill x,y,both,none

#for configuration part you know
def clicked():
    new_text=input.get()
    if len(new_text)>90:
        new_text=new_text[0:30]+'\n'+new_text[30:90]
    mylabel.config(text=new_text)


#button
button = tkinter.Button(text="click me",command=clicked)
button.pack(side="bottom",expand=1)

#like wise the button also contain the command keyword for button operation you know
#Entry
input = tkinter.Entry(cursor="none",width=50,font="italic",background="lightblue")
input.pack(side="top",expand=1)

#for getting the entry from the field get()
#packer is one of Tk'S GEOMETRY MANAGEMENT MECHANISMS.
#The size of any master widget is determined by the size of slave widgets
#Here pack() method can be called with keyword option where the widget is to appear within the container
#This will be the last line of code for making the window in the form of loop

window.mainloop()

