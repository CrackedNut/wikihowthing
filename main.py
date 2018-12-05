from tkinter import *
import requests
from bs4 import BeautifulSoup
import webbrowser
from PIL import Image, ImageTk
import os
from .imgdownloader import DownloadImages

class Window:
    def __init__(self, master):

        self.igc = DownloadImages()

        print("Welcome to the WikiHow random article browser!")

        self.labelimage = None
        self.labeltext = StringVar()

        self.articleName = Label(master, textvariable=self.labeltext)
        self.articleName.pack()

        self.frame = Frame(master)
        self.frame.pack()

        self.next = Button(self.frame, text="NEXT",
                           fg="green", command=self.RandomArticle)
        self.next.pack(side=LEFT)

        self.hi_there = Button(self.frame, text="OPEN",
                               command=self.openArticle)
        self.hi_there.pack(side=LEFT)

        self.quit = Button(self.frame, text="QUIT",
                           fg="red", command=self.Quitting)
        self.quit.pack(side=LEFT)

        self.photolabel = Label(master, image=self.labelimage)
        self.photolabel.pack()

    def Quitting(self):
        self.igc(self.igc.getPaths())
        self.frame.quit()

    def openArticle(self):
        webbrowser.open_new_tab(self.url)

    def getImage(self, s):

        imgs = self.igc.getImages(s)
        photo = Image.open(imgs[1])
        photo = photo.resize((300, 250), Image.ANTIALIAS)
        self.labelimage = ImageTk.PhotoImage(photo)
        self.photolabel.configure(image=self.labelimage)
        self.photolabel.image = self.labelimage



    def RandomArticle(self):
        response = requests.get("https://www.wikihow.com/Special:Randomizer")
        pageurl = response.url
        soup = BeautifulSoup(response.content, "html.parser")
        self.url = soup.find_all("h1")[0].a["href"][2:]
        self.labeltext.set(soup.find_all("h1")[0].a.text)
        self.getImage(soup)


root = Tk()
root.title("Random WikiHow article")
root.geometry("500x300+100+100")

window = Window(root)

root.mainloop()
root.destroy()
