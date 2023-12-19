#Chitleen Kohli
#importing tkinter
from tkinter import *
#for formatting the button
from tkinter import messagebox

#create a window
root = Tk()

#give the window a name in the title bar
root.title("Height")

#setting the window size
root.geometry("300x150")

#writing text
title = Label(root,text = "What is your height?")
question1 = Label(root, text = "Feet:")
question2 = Label(root, text = "Inches:")

#getting user input
text1 = Entry(root, bd = 1)
text2 = Entry(root, bd =1)

#defining the button so a message appears on the screen
def click_calculateCm():
    global text1
    feetString = text1.get()
    global text2
    inchesString = text2.get()
    #converting user input as string to float for calculations
    feet = float(feetString)
    inches = float(inchesString)
    #converting height
    newInches = feet*12.00
    totalInches = inches+newInches
    height = totalInches*2.54
    #converting float to string again for printing it out in the messagebox
    heightString = str(height)
    #showing the messagebox
    messagebox.showinfo(message = ("Your height is "+heightString+" cm."))

#creating the button for calculate cm
calculateCm = Button(text = "Calculate cm", command = click_calculateCm)

#displaying everything on the screen, expect the button
title.pack()
question1.place(x=10,y=30)
text1.place(x=60,y=30)
question2.place(x=10,y=60)
text2.place(x=60,y=60)
calculateCm.pack(side = BOTTOM)

#run the event loop
root.mainloop()
