import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube, Playlist


window = tk.Tk()
window.title('Youtube Downloader')

def widgets():

#from playlist
    destination_of_playlist = Label(window, text='Playlist link:', relief=GROOVE).grid(row=3)
    fromPlaylist = Entry(window,text = 'Enter link', textvariable=playlist_link, width=20, font= 'Arial 14').grid(row=3,column=1, pady=10, padx=30)
    playlist_downlaod = Button(window, text = 'Download', command=playlist_download).grid(row=3, column=2)
    destination_from_playlist = Label(window, text='Destination:', relief=GROOVE).grid(row=4)
    fromPlaylist_browse = Entry(window,text = 'From Playlist', textvariable=download_Path, width=25, font= 'Arial 14').grid(row=4,column=1, padx=10)
    browse_button_Playlist = Button(window, text = 'Browse', command=Browse).grid(row=4, column=2)
    empty_row_playlist = Label(window, text='\n').grid(row=5)

#from link
    destination_of_link = Label(window, text='Video link:', relief=GROOVE).grid(row=6)
    fromLink = Entry(window,text = 'Enter link', textvariable=video_Link, width=20, font= 'Arial 14').grid(row=6,column=1, pady=10, padx=30)
    link_downlaod = Button(window, text = 'Download', command=link_download).grid(row=6, column=2)
    destination_from_link = Label(window, text='Destination:', relief=GROOVE).grid(row=7)
    fromLink_browse = Entry(window, text = 'From Link', textvariable=download_Path, width=25, font= 'Arial 14').grid(row=7,column=1, padx=10)
    browse_button_Link = Button(window, text = 'Browse', command=Browse).grid(row=7, column=2)

def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_Directory)

def link_download():
    Youtube_link = video_Link.get()
    download_folder = download_Path.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.filter(progressive = True, file_extension='mp4').order_by('resolution').desc().first().download(download_folder)

def playlist_download():
    Youtube_link_playlist = playlist_link.get()
    download_folder = download_Path.get()
    getPlaylist = Playlist(Youtube_link_playlist)
    for video in getPlaylist.videos:
        video.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first().download(download_folder)


download_Path = StringVar()
file_location = StringVar()
video_Link = StringVar()
playlist_link = StringVar()

widgets()
window.geometry('500x300')
window.resizable(False,False)
window.mainloop()

