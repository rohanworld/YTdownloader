# Building YT Downloader
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as tmsg
from pytube import YouTube

root = Tk()
root.geometry("733x434")
root.title("YTD by Rohan")
root.columnconfigure(0, weight = 1)

foldername = ""
def openlocation():
    global foldername
    foldername = filedialog.askdirectory()
    if (len(foldername)> 1):
        locationError.config(text=foldername, fg="green")
    else:
        locationError.config(text="Please Choose Folder", fg="red")

def downloadvideo():
    choice = ytdchoices.get()
    url = ytdentry.get()

    if (len(url)>1):
        yt = YouTube(url)

        if (choice==choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif (choice==choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            select = yt.streams.filter(progressive=True, file_extension="mp4").last()     
    select.download(foldername)


ytdlabel = Label(root, text="Paste the Video URL below", font="helvetica 15").grid()

ytdentry = StringVar()
ytdentry = Entry(root, width=100, textvariable=ytdentry).grid()

# ytderror= Label(root, text="Error Message", fg="red").grid( )

savelabel = Label(root, text="Save File..", font="Helvetica 15").grid()

savefile = Button(root,width=10, bg="black",fg="white", text="Choose Path", cursor="hand2", font="bold").grid()

ytdquality = Label(root, text="Select Video Quality", font="Helvetica 18").grid()

choices = ("720p", "144p", "Audio")
ytdchoices = ttk.Combobox(root, values=choices).grid()

download = Button(root,width=10, bg="White",fg="black", text="Download", cursor="hand2", font="bold").grid()



root.mainloop()