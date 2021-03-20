#Project created by the following lovely people
# Dan Hrubec
# Devesh Patel
# Timothy Villaraza

#Project created for the following event: The Second H-Act



#importing gui libraries for main
import tkinter as tk
from tkinter import *
import os

#importing the other files
#whenever we need to add them do it here


def launchFunc():
    print('bigJUICY')

def displayDescription():
    print('primal bad')



if __name__ == "__main__":
    #creating window
    root = tk.Tk()
    root.title("Twitter Spotify Playlist : Launch")
    #default size
    root.geometry("800x600")

    #Welcome text controls
    welcometxt = Label(root, text='Welcome!\nTwitter+Spotify=Playlist')
    welcometxt.config(font=('Ink Free',35))
    welcometxt.pack()

    #Description button controls
    projDescBtn = Button(root, text='Description')
    projDescBtn.config(command=displayDescription)
    projDescBtn.config(font=('Ink Free',35,'bold'))
    projDescBtn.config(bg='#d9d9d9')
    projDescBtn.config(activebackground='#8f8f8f')
    projDescBtn.config(activeforeground='#ffffff')
    projDescBtn.place(x=265,y=250)

    #launch button controls
    launchButton = Button(root, text='Launch Application')
    launchButton.config(command=launchFunc)
    launchButton.config(font=('Ink Free',35,'bold'))
    launchButton.config(bg='#d9d9d9')
    launchButton.config(activebackground='#8f8f8f')
    launchButton.config(activeforeground='#ffffff')
    launchButton.place(x=185,y=400)
    #launchButton.pack()



    #run it down
    root.mainloop()

import TEST

TEST.test()
