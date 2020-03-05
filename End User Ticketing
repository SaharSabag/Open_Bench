from tkinter import *
import tkinter as tk
import getpass

root = Tk()

username = getpass.getuser()
print(username)

def printMessage(event):

    print("This works")

def text():
    print("Message Printed")

def create_window():

    window = tk.Toplevel(root) # Create Window

    windowSize = window.geometry('250x250') # Adjust Size
    window.configure(background='white') # Set Background

    menu = Menu(window) # Place Sub Menu
    window.config(menu=menu)
    subMenu = Menu(menu)
    menu.add_cascade(label='File', menu=subMenu)
    subMenu.add_command(label='New File', command=printMessage)

    Quit = Button(window, text="Quit", command=window.destroy) # Quit
    Quit.pack(side=BOTTOM)


################## GUI ###########################

label = Label(root, text= 'Welcome ' + username, bg='steel blue', fg='white')
label.config(font=("Courier", 12))
label.pack()
frame = Frame(root)
frame.pack()

masterWindow = root.geometry('600x550')
root.configure(background='steel blue')

photo = PhotoImage(file="Logo.PNG")
w = Label(root, image=photo)
w.pack()

########## Side Bar Menus ################

menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New File', command=printMessage)

############# BUTTONS ###############

button_1 = Button(root, text="Open Ticket", bg="white", fg="black", height=1, width=15)
button_1.bind("<Button-1>", printMessage)

button_2 = Button(root, text="Get Alarm Data", bg='white', fg='black', height=1, width=15)
button_2.bind("<Button-1>", printMessage)

button_open_window = Button(root, text='Open Window', command=create_window, bg='white', fg='black')

testButton = Button(root, text='Test', command=text, height=1, width=15) # Enable in a different window - Call a different source while maintaining original window

quitButton = Button(root, text="Quit", command=frame.quit)

button_1.pack(padx=10, pady=10)  # SIDE: RIGHT, LEFT, BOTTOM, TOP || FILL: X,Y || PADx=1-100, PADy=1-100
button_2.pack()
button_open_window.pack(padx=10, pady=10)
testButton.pack()
quitButton.pack(padx=10, pady=10)

############### Status Bar ############

status = Label(root, text="Preparing to do Nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
