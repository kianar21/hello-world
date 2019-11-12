import PIL
import matplotlib.pyplot as plt
import os.path
import numpy as np

directory = os.path.dirname(os.path.abspath(__file__))
minion_file = os.path.join(directory, 'minion.jpg')
img = plt.imread(minion_file)

##################################

height = len(img)
width = len(img[0])

for column in range (0,24):
    for row in range (0,4032):
        img[row][column] = [0, 255, 255]
for column in range (3000,3024):
    for row in range (2016,4032):
        img[row][column] = [0, 255, 255]

for column in range (3000,3024):
    for row in range (0,2015):
        img[row][column] = [0, 255, 255]

for column in range (0,3024):
    for row in range (4008,4032):
        img[row][column] = [255, 0, 255]
        
for column in range (0,3024):
    for row in range (0,24):
        img[row][column] = [255, 0, 255]

##################################

img2 = PIL.Image.fromarray(img)

img3 = img2.transform((3024, 4032), PIL.Image.QUAD,
(50,50,4000,1000,3002,4002,1000,4000,4000,4000) )

img4 = img3.rotate(270, expand=True)

##################################
       
fig, ax = plt.subplots(1, 1)
ax.imshow(img4)
fig.show()

(50,55,2500,2500,302,302,50,3000,3000,4000)
(50,55,2500,2500,302,302,1000,3000,3000,4000)
(50,50,4000,1000,3002,4002,1000,4000,4000,4000) 