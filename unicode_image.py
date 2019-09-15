import numpy as np
from PIL import Image

img = input("input file name: ")
width = int(input("How wide should the image be: "))
height = int(input("How tall should the image be: "))
ask = True
want = False
while ask:
        yesOrNo = input("Do you want to chose your own unicode charecters: ")
        if yesOrNo != "yes" and yesOrNo != "no":
                yesOrNo = input("Do you want to chose your own unicode charecters: ")
        elif yesOrNo == "yes" or yesOrNo == "no":
                ask = False
                if yesOrNo == "yes":
                        want = True
                elif yesOrNo == "No":
                        want = False        
if want == True:
        charecter1 = input("Darkest: ")
        charecter2 = input("Second darkest: ") 
        charecter3 = input("Third darkest: ")
        charecter4 = input("Second lightest: ")
        charecter5 = input("Lightest: ")
x = Image.open(img,'r') #opens the given image
x = x.resize((width, height)) #resizes it to given dementions 
x = x.convert('L') #makes it greyscale
y = np.asarray(x.getdata(),dtype=np.float64).reshape((x.size[1],x.size[0])) #return array of greyscale values
grL = y

def to_unicode(grey):
        if want == True:        
                if grey > 0.8 * 255:
                        return charecter1
                elif grey > 0.6 * 255:
                        return charecter2
                elif grey > 0.4 * 255:
                        return charecter3
                elif grey > 0.2 * 255:
                        return charecter4        
                elif grey >= 0 * 255: 
                        return charecter5
        if want == False:
                if grey > 0.8 * 255:
                        return "#"

                elif grey > 0.6 * 255:
                        return "-"

                elif grey > 0.4 * 255:
                        return "/"

                elif grey > 0.2 * 255:
                        return "^"
                
                elif grey >= 0 * 255: 
                        return "'"
                
big_list = []
file = open(img[:-3]+"txt","w")

for i in grL:
        for j in i:
                # print("made it here")
                big_list.append(j)

for i in range(len(big_list)):
        file.write(to_unicode(big_list[i]))
        if (i+1) % width == 0:
                file.write("\n") 



