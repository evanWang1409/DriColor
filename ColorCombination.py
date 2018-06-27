import requests
from bs4 import BeautifulSoup
import re
import webcolors

class ColorCombination:

    combNum = 3;


#--------
#   Get the urls for 'combNum' number of works with a from a given url searching
#   for a certain color
#--------
    def findShots(self, url):
        s = requests.session()
        p = requests.get(url)
        soup = BeautifulSoup(p.content, 'html5lib')
        pattern = re.compile(r'\"\/shots\/.*\"')
        taglist = []
        urlRes = []
        
        for t in soup.ol:
            if t.name == 'li':
                taglist.append(t)
		
        count = 0
	
        for tag in taglist:
            arr = pattern.findall(str(tag))
            url1 = 'http://dribbble.com'
            url2 = arr[0][1 : len(arr[0]) - 1]
            urlRes.append(url1 + url2)
            count = count + 1
            if(count == self.combNum):
                break
        
        return urlRes


#--------
#   Get the color combination of a work with the url of that work
#--------
    def ColorCombFromShots(self, url):
        s = requests.session()
        p = requests.get(url)
        soup = BeautifulSoup(p.content, 'html5lib')
        
        tag = soup.find_all('ul', class_ = 'color-chips group')
        pattern = re.compile(r'background-color: #......')
        colorList = []
        tempList = pattern.findall(str(tag))
        
        for key in tempList:
            colorList.append(key[18:])

        return colorList


#--------
#   Get the color combination for a given color hex
#--------
    def findColorComb(self, color):
        colorNum = color[1:]
        url2 = colorNum
        url1 = 'http://dribbble.com/colors/'
        url = url1 + url2
        
        colorCombList = []
        for shotUrl in self.findShots(url):
            colorCombList.append(self.ColorCombFromShots(shotUrl))

        return colorCombList



#--------
#   Get the rgb values for colors in a color combination
#--------
    def getColorCombRgb(self, colorComb):
        rgbList = []

        for color in colorComb:
            r,g,b = webcolors.hex_to_rgb(color)
            rgbList.append([r,g,b])

        return rgbList


#--------
#   The main function for finding 'combNum' number of color combinations and
#   store their rgb values
#--------
    def getAllColorComb(self, color):
        colorCombs = self.findColorComb(color)
        colorCombsRgb = []
        count = 0
        for colorComb in colorCombs:
            colorCombsRgb.append(self.getColorCombRgb(colorComb))
            count = count + 1
            if count == self.combNum:
                break

        return colorCombsRgb
        
