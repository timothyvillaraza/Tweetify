#Project created by the following lovely people
# Dan Hrubec
# Devesh Patel
# Timothy Villaraza

#Project created for the following event: The Second H-Act


#importing gui libraries for main
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import threading

#importing the other files
import twitter
import spotify

def createPlaylist():
    spotify.setusername(entry.get())
    th = threading.Thread(target=spotify.generatePlaylist)
    th.start()

def progressScreen():
    progressReport = tk.Toplevel()
    progressReport.geometry("800x600")

    querylbl = Label(progressReport)
    querylbl.config(font=('Proxima Nova', 20,'bold'))
    querylbl.pack()

    artistlbl = Label(progressReport)
    artistlbl.config(font=('Proxima Nova', 15))
    artistlbl.pack()

    prgbar = Progressbar(progressReport, orient=HORIZONTAL,length=500,mode='determinate')
    prgbar.place(x=150,y=400)

    beginButton = Button(progressReport,text='Begin')
    beginButton.config(font=('Proxima Nova', 15, 'bold'))
    beginButton.config(bg='#d9d9d9')
    beginButton.config(activebackground='#8f8f8f')
    beginButton.config(activeforeground='#ffffff')
    beginButton.place(x=350, y=450)
    beginButton.config(command=createPlaylist)

    exitbtn = Button(progressReport,text='Exit')
    exitbtn.config(font=('Proxima Nova', 15, 'bold'))
    exitbtn.config(bg='#d9d9d9')
    exitbtn.config(activebackground='#8f8f8f')
    exitbtn.config(activeforeground='#ffffff')
    exitbtn.place(x=358, y=510)
    exitbtn.config(command=lambda : progressReport.destroy())
    exitbtn.config(state=DISABLED)

    querycount = 0
    artists = {}
    messageFlag = False

    def update():
        """
        Called every second in a half to display loading information
        """
        querycount = twitter.getCounter()
        artists = twitter.getArtistDict()
        artists = dict(sorted(artists.items(), key=lambda x: x[1], reverse=True))
        top_10_artists = list(artists.keys())
        top_10_artists = top_10_artists[:10]
        lblstring = str(querycount) + " tweets have been analyzed so far.\n"

        artiststring = ""
        for art in top_10_artists:
            artiststring = artiststring + str(artists[art]) + " mentions of " + art + ".\n"

        prgbar['value'] = int((querycount/500) * 100)
        querylbl.config(text=lblstring)
        artistlbl.config(text=artiststring)

        if querycount > 0:
            beginButton.config(state=DISABLED)


        if querycount == 500:
             exitbtn.config(state=NORMAL)
             tk.messagebox.showinfo('Complete','Playlist generated. Check your spotify.\nhttps://accounts.spotify.com/')
        else:
            progressReport.after(1500, update)

    update()
    progressReport.mainloop()


def launchFunc():
    """
    Starts a new thread for the loading screen
    """
    th = threading.Thread(target=progressScreen)
    th.start()


def displayDescription():
    desc = tk.Toplevel()
    desc.title('Project Description')
    descStr = "\n" \
              "\n" \
              "The goal of the project was to create a Spotify Playlist based off\n" \
              "the current trending artists. To do this we would use Tweepy's\n" \
              "API to look at the most current trends within the music industry and pull\n" \
              "keywords. Once we collected enough data from the trending artists\n" \
              "we would combine this with Spotipy's API to generate a playlist\n" \
              "on the user's Spotify account. With the songs from the latest trends.\n" \
              "\n" \
              "\n" \
              "---Credits---\n" \
              "Developers:\n" \
              "Dan Hrubec\n" \
              "Devesh Patel\n" \
              "Timothy Villaraza\n" \
              "\n" \
              "Logo Design:\n" \
              "Eli Yu"\
              "\n" \
              "\n"
    desclbl = Label(desc,text=descStr)
    desclbl.pack()

entry = Entry


if __name__ == "__main__":
    #creating window
    root = tk.Tk()
    root.title("Tweetify Launch by Dan Hrubec, Devesh Patel, Timothy Villaraza")
    # root.configure(bg="#191414")

    #default size
    root.geometry("800x900")

    #Welcome text controls


    # Tweetify Logo
    canvas = Canvas(root, width=500, height=400)
    img = PhotoImage(file="tweetify.png")
    canvas.create_image(50, 50, anchor=NW, image=img)
    canvas.place(x=160, y=-20)
    canvas.pack()

    #Description button controls
    projDescBtn = Button(root, text='Description')
    projDescBtn.config(command=displayDescription)
    projDescBtn.config(font=('Proxima Nova',35,'bold'))
    projDescBtn.config(bg='#d9d9d9')
    projDescBtn.config(activebackground='#8f8f8f')
    projDescBtn.config(activeforeground='#ffffff')
    projDescBtn.place(x=250,y=450)

    #launch button controls
    launchButton = Button(root, text='Launch Application')
    launchButton.config(command=launchFunc)
    launchButton.config(font=('Proxima Nova',35,'bold'))
    launchButton.config(bg='#d9d9d9')
    launchButton.config(activebackground='#8f8f8f')
    launchButton.config(activeforeground='#ffffff')
    launchButton.place(x=165,y=685)

    usernameprompt = Label(root, text="Enter your spotify username before running:")
    usernameprompt.place(x=275, y=575)

    entry = tk.Entry(root)
    entry.place(x=325, y=600)

    #run it down
    root.mainloop()


