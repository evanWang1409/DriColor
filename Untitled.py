from ColorDetector import ColorDetector

detector = ColorDetector()
image = detector.readImage('/Users/bioadmin/Desktop/WechatIMG546.jpeg')
res = detector.getDominantColors(image, 4)

print res
