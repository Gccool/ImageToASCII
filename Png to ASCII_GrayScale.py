import math
import cv2
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time

startTime = time.time()
Path = r''
Outputfile = open(r"", "w")
img = cv2.imread(Path)

characters = [' ', '.', '_', ':', ';', '~', '1', '5', '#', '@']

Answer = ''

DeScaleAmount = 1
ShouldDeScale = True
#Img = Image.new('RGB', (img.shape[0] * 18, int(img.shape[1] * 10.1)), (0, 0, 0))
#d = ImageDraw.Draw(Img)


i = 0


if ShouldDeScale:
    for y in range(0, int(img.shape[0] / DeScaleAmount)):
        for x in range(0, int(img.shape[1] / DeScaleAmount)):
            b,g,r = (img[y * DeScaleAmount, x * DeScaleAmount])
            luminance = (r * 0.3) + (g * 0.59) + (b * 0.11)
            Char = characters[int(luminance / 40)]
            Answer += Char
            Answer += ' '
            #d.text((x, y), Answer, fill=(r, g, b))
            print(i)
            i += 1
        Answer += '\n'
        
if ShouldDeScale == False:
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            b,g,r = (img[y, x])
            luminance = (r * 0.3) + (g * 0.59) + (b * 0.11)
            Char = characters[int(luminance / 40)]
            Answer += Char
            Answer += ' '
            #d.text((x, y), Answer, fill=(r, g, b))
            print(i)
            i += 1
        Answer += '\n'

if ShouldDeScale:
    Img = Image.new('RGB', (int((img.shape[0] * 18) / DeScaleAmount), int((img.shape[1] * 15.5) / DeScaleAmount)), (0, 0, 0))
if ShouldDeScale == False:
    Img = Image.new('RGB', (int((img.shape[0] * 18)), int((img.shape[1] * 15.5))), (0, 0, 0))
d = ImageDraw.Draw(Img)
d.text((5, 5), Answer, fill=(255, 255, 255))
Img.save(r"")

a = Outputfile.write(Answer)        
Outputfile.close()
print(a)  

EndTime = time.time()

while True:
    print(EndTime - startTime)

        
