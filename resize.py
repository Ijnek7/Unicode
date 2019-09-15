# import numpy as np 

from PIL import Image

img = input("input file name: ")
width = int(input("How wide should the image be: "))
height = int(input("How tall should the image be: "))


x = Image.open(img,'r') #opens the given image
x = x.resize((width, height)) #resizes it to given dementions 
file = file.open(file = open(img[:-3]+"png","w")
file.write(x)




