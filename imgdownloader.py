import os
import requests
from bs4 import BeautifulSoup

class DownloadImages():
    """Documentation for DownloadImages
    """

    def getImages(self, s):
        found = s.find_all("img", {"class": "whcdn content-fill"})
        self.images = []

        for el in found:
            if el.has_attr("data-src"):
                self.images.append(el)

        self.imgsPaths = []

        for i in self.images:
            imgNum = self.images.index(i)
            imgpath = f"./IMAGES/img{imgNum}.jpg"
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

    def getPaths(self):
        return self.imgsPaths
    #def nenPage(self):
