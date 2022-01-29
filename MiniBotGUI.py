from Tkinter import *
import Tkinter as tk


class MiniGUI:

    def __init__(self, master):

        frame = Frame(master)          # TOP FRAME
        frame.pack()                   # Pack Top Frame
        bottomFrame = Frame(master)    # BOTTOM FRAME
        bottomFrame.pack(side=BOTTOM)  # Pack Bottom Frame

        master.geometry('300x250')

        self.disconnectButton = Button(frame,  text='Disconnect',   command=self.disconnectBot, height=5, width=9)  # Disconnect BUTTON
        self.connectButton = Button(frame,     text='Connect',      command=self.connectBot,    height=5, width=9)  # Connect BUTTON
        self.switchState = Button(bottomFrame, text='Switch State', command=self.switchState,   height=5, width=9)  # Switch BUTTON

        self.disconnectButton.pack(side=LEFT)     # Pack Disconnect
        self.connectButton.pack(side=LEFT)        # Pack Connect
        self.switchState.pack(side=BOTTOM)        # Pack Switch Values

    def disconnectBot(self):
        self.label = tk.Label(text='Disconnected !')
        self.label.place(x=110, y=100)
        self.label.after(600, self.clear_label)

        print('Disconnect')

    def connectBot(self):
        self.label = tk.Label(text='Connected !')
        self.label.place(x=120, y=120)
        self.label.after(600, self.clear_label)

        print('Connected')

    def switchState(self):
        self.label = tk.Label(text='Switched Values !')
        self.label.place(x=100, y=130)
        self.label.after(600, self.clear_label)

        print('Switched Values !')

    def clear_label(self):
        print "Label Cleared"
        self.label.place_forget()


root = Tk()
s = MiniGUI(root)
root.mainloop()

