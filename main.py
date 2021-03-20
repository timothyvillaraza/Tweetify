#Project created by the following lovely people
# Dan Hrubec
# Devesh Patel
# Timothy Villaraza

#Project created for the following event: The Second H-Act



#importing gui libraries for main
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import os

#importing the other files
#whenever we need to add them do it here


def launchFunc():
    print('bigJUICY')

def displayDescription():
    desc = tk.Toplevel()
    desc.title('Project Description')
    descStr = "The goal of the project was to create a Spotify Playlist based off\n" \
              "the current trending artists or songs. To do this we would use Twitter's\n" \
              "API to look at the most current trends within the music industry and pull\n" \
              "keywords. Once we collected enough data from the trending artists and song\n" \
              "we would combine this with Spotify's API to generate a shareable playlist\n" \
              "with the songs from the latest trends.\n"
    desclbl = Label(desc,text=descStr)
    desclbl.pack()





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


