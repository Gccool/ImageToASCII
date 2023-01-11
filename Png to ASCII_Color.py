import math
import cv2
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
import colorsys

startTime = time.time()

Path = r'Put Image Her'
Outputfile = open(r"Output Path.txt", "w") #txt one
img = cv2.imread(Path)

characters = [' ', '.', '_', ':', ';', '~', '1', '5', '#', '@']


Answer = ''

Margin = Offset = 40

DeScaleAmount = 1
ShouldDownScale = False

if ShouldDownScale:
    Img = Image.new('RGB', (int((img.shape[0] * 15) / DeScaleAmount), int((img.shape[1] * 15) / DeScaleAmount)), (25, 25, 25))
if ShouldDownScale == False:
    Img = Image.new('RGB', (img.shape[0] * 15, int(img.shape[1] * 15)), (25, 25, 25))
d = ImageDraw.Draw(Img)



i = 0


if ShouldDownScale:
    for y in range(0, int(img.shape[0] / DeScaleAmount)):
        for x in range(0, int(img.shape[1] / DeScaleAmount)):
            b,g,r = (img[y * DeScaleAmount, x * DeScaleAmount])
            luminance = (r * 0.3) + (g * 0.59) + (b * 0.11)
            Char = characters[int(luminance / 40)]
            Answer += Char
            Answer += ' '
            d.text((int((x * 10)) + 5, int((y * 10))), Char, fill=(r, g, b, 255)) #FIX TEXT SCALLING
            #d.text((x, y), Answer, fill=(r, g, b))
            print(i)
            i += 1
        Answer += '\n'
        
if ShouldDownScale == False:
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            b,g,r = (img[y, x])
            luminance = (r * 0.3) + (g * 0.59) + (b * 0.11)
            Char = characters[int(luminance / 40)]
            Answer += Char
            Answer += ' '
            d.text((int(x * 10) + 5, int(y * 10)), Char, fill=(r, g, b, 255)) #FIX TEXT SCALLING
            #d.text((x, y), Answer, fill=(r, g, b))
            print(i)
            i += 1
            
            
        Answer += '\n'

#img = Image.new('RGB', (img.shape[0] * 18, int(img.shape[1] * 10.1)), (0, 0, 0))
#d = ImageDraw.Draw(img)
#d.text((5, 5), Answer, fill=(255, 255, 255))
Img.save(r"OutputLocation.png")

a = Outputfile.write(Answer)        
Outputfile.close()
print(a)  

EndTime = time.time()
print(EndTime - startTime)


time.sleep(999999)
        
