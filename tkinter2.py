from tkinter import *

# recall the tkinter which is basically a module used to make the fun parts you know 
# firstly we need to create the window from TK() and title and minsize what ever it is
# window and label and button and pack() and we can give the text and font in the command used for the actionlistener and whatever it is
# entry which is insert and get() and text ( which is textfield which you can write what ever it is)
# window 


screen =Tk()
screen.title("Widget Examples")
screen.minsize(width=300,height=500)

#Labels
label = Label(text="This is label",state="active",font=("sans-sarif",19,"bold"),underline=1)
#For chaning label.config(text="This is new text")
label.pack()

def action():
    print("Do someting")

#button
butt = Button(text="Click me!")
butt.pack()

#entry
entry = Entry(width=30) #width(30)
#default string insert
entry.insert(END,string="Some text to begin with.")
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)

#cursor on the line
text.focus()

#Adds some text begin with
text.insert(END,"Example of multi-line text entry")
text.pack()

def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0 ,to=10,width=5,command=spinbox_used)
spinbox.pack()

#checkbox
checked_state = IntVar() #This is used for capturing the value of current state
#Here the IntVar is the class from master packagee
checkbutton = Checkbutton(text="Is On?")
print(checked_state.get())
checkbutton.pack()

#radio_button
radio_state = IntVar()
radiobutton1 = Radiobutton(text = "Option1",value=1,variable=radio_state)
radiobutton2 = Radiobutton(text = "Option2",value=2,variable=radio_state)
radiobutton1.pack()
radiobutton2.pack()

#listBox

#HERE WE HAVE THE Checkbutton(text = "") and Radiobutton() and Listbox()
def listbox_used(event):
    print(list.get(list.curselection()))

list = Listbox(height=4)
friends = ["harshen","somu","vishal","selva"]

for item in friends:
    list.insert(friends.index(item),item)

list.bind("<<ListboxSelect>>",listbox_used)
list.pack()

#screen in loop
screen.mainloop()