# OBJECTIVE:

# Use I:\ for local and GER\USER for remote access

## Find TC Alarms in TC/TA
## Def Fetch Files, Print and Send them

from tkinter import *
import tkinter as tk
import time
import getpass


# connection = sql.connect("company.db") ## Enter GEDI Domain Data Base

username=getpass.getuser()#Getuserdata

root = Tk()


def doNothing():
    print("okay okay I won't")

def fetchfiles():

    # APpath = ('') # Dynamic for each collateral. ## PARTIAL PATH
    print("Fetching Files..")

    with open(APpath, 'r') as f:

        global print_label


        print("Files Fetched")

        print_label = Label(root, text='Alright', bg='grey', fg='white').grid(row=17)
        # time.sleep(2)
        print('done')


def create_window():

    window = tk.Toplevel(root)  # Create Window
    window.title("")


    window.mainloop()


menu = Menu(root) # Associate subs to each SP
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="1713", command=doNothing)
subMenu.add_command(label="1768", command=doNothing)
subMenu.add_command(label="2466", command=doNothing)
subMenu.add_command(label="2707", command=doNothing)
subMenu.add_command(label="Coming Soon", command=doNothing)
# subMenu.add_separator() ## Creates a line..
subMenu.add_command(label="Exit", command=doNothing)


masterWindow = root.geometry('710x900')
root.configure(background='grey')



PNB5 = Button(root, bg='royalblue2', width=100, height=2, text="PNB 5", borderwidth=5, relief=RAISED).grid(row=0)


AP501 = Button(root, width=30, height=2, text="AP 501", borderwidth=5, relief=RAISED, command=create_window).grid(row=1, sticky=E)
AP502 = Button(root, width=30, height=2, text="AP 502", borderwidth=5, relief=RAISED).grid(row=1, sticky=W)


TESTER501 = Button(root, width=30, height=2, text="TESTER 501", borderwidth=5, relief=RAISED).grid(row=1, sticky=N)
TESTER502 = Button(root, width=30, height=2, text="TESTER 502", borderwidth=5, relief=RAISED).grid(row=2, sticky=N)

TIU501 = Button(root, width=30, height=2, text="TIU 501", borderwidth=5, relief=RAISED).grid(row=2, sticky=E)
TIU502 = Button(root, width=30, height=2, text="TIU 502", borderwidth=5, relief=RAISED).grid(row=2, sticky=W)



PNB4 = Button(root, bg='royalblue2', width=100, height=2, text="PNB 4", borderwidth=5, relief=RAISED).grid(row=3)

AP401 = Button(root, width=30, height=2, text="AP 401", borderwidth=5, relief=RAISED).grid(row=4, sticky=E)
AP402 = Button(root, width=30, height=2, text="AP 402", borderwidth=5, relief=RAISED).grid(row=4, sticky=W)

TESTER401 = Button(root, width=30, height=2, text="TESTER 401", borderwidth=5, relief=RAISED).grid(row=4, sticky=N)
TESTER402 = Button(root, width=30, height=2, text="TESTER 402", borderwidth=5, relief=RAISED).grid(row=5, sticky=N)

TIU401 = Button(root, width=30, height=2, text="TIU 402", borderwidth=5, relief=RAISED).grid(row=5, sticky=E)
TIU402 = Button(root, width=30, height=2, text="TIU 401", borderwidth=5, relief=RAISED).grid(row=5, sticky=W)



PNB3 = Button(root, bg='royalblue2', width=100, height=2, text="PNB 3", borderwidth=5, relief=RAISED).grid(row=6)

AP301 = Button(root, width=30, height=2, text="AP 301", borderwidth=5, relief=RAISED).grid(row=7, sticky=E)
AP302 = Button(root, width=30, height=2, text="AP 302", borderwidth=5, relief=RAISED).grid(row=7, sticky=W)

TESTER301 = Button(root, width=30, height=2, text="TESTER 301", borderwidth=5, relief=RAISED).grid(row=7, sticky=N)
TESTER302 = Button(root, width=30, height=2, text="TESTER 302", borderwidth=5, relief=RAISED).grid(row=8, sticky=N)

TIU301 = Button(root, width=30, height=2, text="TIU 301", borderwidth=5, relief=RAISED).grid(row=8, sticky=E)
TIU302 = Button(root, width=30, height=2, text="TIU 302", borderwidth=5, relief=RAISED).grid(row=8, sticky=W)



PNB2 = Button(root, bg='royalblue2', width=100, height=2, text="PNB 2", borderwidth=5, relief=RAISED).grid(row=9)

AP201 = Button(root, width=30, height=2, text="AP 201", borderwidth=5, relief=RAISED).grid(row=10, sticky=E)
AP202 = Button(root, width=30, height=2, text="AP 202", borderwidth=5, relief=RAISED).grid(row=10, sticky=W)

TESTER201 = Button(root, width=30, height=2, text="TESTER 201", borderwidth=5, relief=RAISED).grid(row=10, sticky=N)
TESTER202 = Button(root, width=30, height=2, text="TESTER 202", borderwidth=5, relief=RAISED).grid(row=11, sticky=N)

TIU201 = Button(root, width=30, height=2, text="TIU 201", borderwidth=5, relief=RAISED).grid(row=11, sticky=E)
TIU202 = Button(root, width=30, height=2, text="TIU 202", borderwidth=5, relief=RAISED).grid(row=11, sticky=W)



PNB1 = Button(root, bg='royalblue2', width=100, height=2, text="PNB 1", borderwidth=5, relief=RAISED).grid(row=12)

AP101 = Button(root, width=30, height=2, text="AP 101", borderwidth=5, relief=RAISED).grid(row=13, sticky=E)
AP102 = Button(root, width=30, height=2, text="AP 102", borderwidth=5, relief=RAISED).grid(row=13, sticky=W)

TESTER101 = Button(root, width=30, height=2, text="TESTER 101", borderwidth=5, relief=RAISED).grid(row=13, sticky=N)
TESTER102 = Button(root, width=30, height=2, text="TESTER 102", borderwidth=5, relief=RAISED).grid(row=14, sticky=N)

TIU101 = Button(root, width=30, height=2, text="TIU 101", borderwidth=5, relief=RAISED).grid(row=14, sticky=E)
TIU102 = Button(root, width=30, height=2, text="TIU 102", borderwidth=5, relief=RAISED).grid(row=14, sticky=W)

Module = Button(root, bg='royalblue2', width=100, height=3, text="Module", borderwidth=5, relief=RAISED).grid(row=15)

FF = Button(root, bg='black', fg='white', width=50, height=2, text="Check Connection", borderwidth=4, relief=RAISED, command=fetchfiles).grid(row=16)


root.mainloop()


