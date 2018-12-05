import requests
from bs4 import BeautifulSoup
import os

class DownloadImages():
    def __init__(self):
        response = requests.get('https://www.wikihow.com/Special:Randomizer')
        self.soup = BeautifulSoup(response.content, "html.parser")
        #getImages(self.soup)

    def getImages(self, s):
        found = s.find_all("img", {"class": "whcdn content-fill"})
        self.images = []

        for el in found:
            if el.has_attr("data-src"):
                self.images.append(el)

        self.imgsPaths = []

        for i in self.images:
            imgNum = self.images.index(i)
            imgpath = f"./IMAGESTEST/img{imgNum}.jpg"
            self.imgsPaths.append(imgpath)

            try:
                downloaded = requests.get(i["data-src"])
                img = downloaded.content
            except:
                continue
            with open(imgpath, "wb") as f:
                try:
                    f.write(img)
                except Exception as e:
                    print(e)
        return self.imgsPaths

    def deleteImages(self, s):
        for el in s:
            if os.path.exists(el):
                os.remove(el)
            else:
                print("file doesnt' exist")

if __name__ == "__main__":
    response = requests.get('https://www.wikihow.com/Special:Randomizer')
    soup = BeautifulSoup(response.content, "html.parser")
    thing = DownloadImages()
    paths = thing.getImages(soup)
    input("del:")
    thing.deleteImages(paths)
