import os
import numpy as np
cwd = os.getcwd()

from PIL import Image

im = Image.open("test.png")

print("I am Branch")

width, height = im.size

print(width,height)

#im.show()

mylist = list(np.asarray(im))

mylist2 = mylist[0]

mylist3 = mylist[1][-1]

print(mylist2)

print(mylist3)