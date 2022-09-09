from doctest import master
from email.mime import image
import tkinter
import tkinter.messagebox
from tkinter.tix import COLUMN, ROW
import customtkinter
from customtkinter import CTkEntry
import sys
from pytube import YouTube
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("350x550")
video_pic = tkinter.PhotoImage(file='./assets/video.png')
audio_pic = tkinter.PhotoImage(file='./assets/mp4.png')


#--------------------------------------------------------------------------------------------------------------#


label = customtkinter.CTkLabel(master=app, text="Bret's Youtube Downloader", text_font=(
    "Helvetica", 17), width=120, height=25, corner_radius=8)
label.pack(padx=15, pady=40)

link = customtkinter.CTkEntry(master=app, placeholder_text="Paste Youtube link here",
                              width=270, height=30, border_width=2, corner_radius=10)
link.place(x=40, y=95)


#--------------------------------------------------------------------------------------------------------------#
# FRAMES


downloadFrames = customtkinter.CTkFrame()
downloadFrames.place(relx=0.1, rely=0.1, anchor=link.place())
# downloadFrames.pack(pady=20)
downloadFrames.place(x=53, y=105)


#--------------------------------------------------------------------------------------------------------------#


def downloadVideo():
    link_string = CTkEntry.get(link)
    yt = YouTube(link_string)
    quality = yt.streams.get_highest_resolution()
    quality.download()


def downloadAudio():
    link_string = CTkEntry.get(link)
    yt = YouTube(link_string)
    quality = yt.streams.get_audio_only()
    quality.download()


#--------------------------------------------------------------------------------------------------------------#


videoButton = customtkinter.CTkButton(
    master=downloadFrames, text="Download Video", command=downloadVideo)
videoButton.pack(padx=17, pady=17)

audioButton = customtkinter.CTkButton(
    master=downloadFrames, text="Download Audio", command=downloadAudio)
audioButton.pack(pady=17)

#--------------------------------------------------------------------------------------------------------------#


app.resizable(0, 0)
app.mainloop()
