from ColorDetector import ColorDetector
from ColorCombination import ColorCombination

detector = ColorDetector()
combinator = ColorCombination()
image = detector.readImage('/Users/bioadmin/Desktop/WechatIMG30.jpeg')
colorList = detector.getDominantColors(image, 4)
colorCombsRgb = []
for color in colorList:
    colorCombsRgb.append(combinator.getAllColorComb(color))
for comb in colorCombsRgb:
    for colorComb in comb:
        print colorComb
        print '\n'
    print '\n'
