from tkinter import *


#mile to kilometer (1 to 1.609344)

#Screen
window = Tk()
window.title("converters")
window.minsize(width=300,height=400)


#Miles
miles = Label(text="Miles",font=("Arial",10,"bold"))
entry1 = Entry(width=10,background="coral",border=1,font=("Arial",10,"bold"))
miles.grid(column=2,row=30)
entry1.grid(column=3,row=30)
to1 = Label(text="to",font=("Arial",10,"bold"),)
to1.grid(column=4,row=30)

#kilometer
kilometer = Label(text="kilometers", font=("Arial",10,"bold"))
kilometer.grid(column=5,row=30)
entry2 = Entry(width=10,background="coral",border=1,font=("Arial",10,"bold"))
entry2.grid(column=6,row=30)
butt_miles1 = Button(text="Calculate",borderwidth=2)
butt_miles1.grid(column=10,row=30)

#reverse and error
error1=Label(text="")
error1.grid(column=5,row=40)
butt_reverse1=Button(text="Reverse")
butt_reverse1.grid(column=5,row=45)


#meter
meter = Label(text="Meter",font=("Arial",10,"bold"))
entry3 = Entry(width=10,background="coral",border=1,font=("Arial",10,"bold"))
meter.grid(column=2,row=80)
entry3.grid(column=3,row=80)
to1 = Label(text="to",font=("Arial",10,"bold"),)
to1.grid(column=4,row=80)

#kilometer
kilometer = Label(text="kilometers", font=("Arial",10,"bold"))
kilometer.grid(column=5,row=80)
entry4= Entry(width=10,background="coral",border=1,font=("Arial",10,"bold"))
entry4.grid(column=6,row=80)
butt_miles2 = Button(text="Calculate",borderwidth=2)
butt_miles2.grid(column=10,row=80)

#reverse and error
error2=Label(text="")
error2.grid(column=5,row=90)
butt_reverse2=Button(text="Reverse")
butt_reverse2.grid(column=5,row=97)


#Foot
Foot = Label(text="Foot",font=("Arial",10,"bold"))
entry5 = Entry(width=10,background="coral",border=1,font=("Arial",10,"bold"))
Foot.grid(column=2,row=100)
entry5.grid(column=3,row=100)
to1 = Label(text="to",font=("Arial",10,"bold"),)
to1.grid(column=4,row=100)

#meter
meter1 = Label(text="Meter",font=("Arial",10,"bold"))
entry6 = Entry(width=10,background="coral",border=1,font=("Arial",10,"bold"))
meter1.grid(column=5,row=100)
entry6.grid(column=6,row=100)
butt_miles3 = Button(text="Calculate",borderwidth=2)
butt_miles3.grid(column=10,row=100)

#reverse and error
error=Label(text="")
error.grid(column=5,row=110)
butt_reverse3=Button(text="Reverse")
butt_reverse3.grid(column=5,row=120)



#exit
window.mainloop()