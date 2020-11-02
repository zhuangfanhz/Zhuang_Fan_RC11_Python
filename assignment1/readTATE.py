# Imports:
# use python --version to check what version of python your standard installation is
# if this is 2.x you will have to use pip3 install otherwise pip install

import csv
import requests
# pip install pillow
from PIL import Image
from io import BytesIO

# Define the ArtTate class, with all attributes that you find usefull
class ArtTate:
    def __init__(self, id, year, acquisitionYear, width, depth, height, imageUrl, artist):
        self.id = id
        self.year = year
        self.acquisitionYear = acquisitionYear
        self.width = width
        self.depth = depth
        self.height = height
        self.imageUrl = imageUrl
        self.artist = artist
        self.imagePath = ''

        if self.width:
            try:
                self.width = float(self.width)
            except ValueError:
                self.width = 10
        else:
            self.width = 10

        if self.height:
            try:
                self.height = float(self.width)
            except ValueError:
                self.height = 10
        else:
            self.height = 10

        if self.depth:
            try:
                self.depth = float(self.width) 
            except ValueError:
                self.depth = 10
        else:
            self.depth = 10

    def describe(self):
        print("artist:" + self.artist, "id:" + self.id,"year:" + self.year, "acquisitionYear:" + self.acquisitionYear, "width:" + str(self.width), "depth:" + str(self.depth), "height:" + str(self.height))

    def getImageFile(self):
        if self.imageUrl:
            response = requests.get(self.imageUrl)
            try:
                im = Image.open(BytesIO(response.content))
            except OSError:
                return None
            path = "C:\\Users\\hp\\Documents\\GitHub\Zhuang_Fan_RC11_Python\\Assignment1\\Artimages\\ "+ "id_"+ self.id+ "_year_"+ self.year+ ".jpg"
            self.imagePath = path
            im.save(path, "JPEG")

artPieces = []
with open("C:\\Users\\hp\\Documents\\GitHub\\Zhuang_Fan_RC11_Python\Assignment1\\CSVFiles\\artwork_data.csv", encoding = 'utf-8-sig') as artFile:
    artReader = csv.DictReader(artFile)

    for row in artReader:
        id = row['id']
        year = row['year']
        acquisitionYear = row['acquisitionYear']
        width = row['width']
        height = row['height']
        depth = row['depth']
        imageUrl = row['thumbnailUrl']
        artist = row['artist']

        if width or depth or height:
            artPiece = ArtTate(id, year, acquisitionYear, width, depth, height, imageUrl, artist)
            artPieces.append(artPiece)

for art in artPieces:
    if "1921" in art.acquisitionYear:
        art.getImageFile()
