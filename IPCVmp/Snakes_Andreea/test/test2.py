import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

filename = 'cropped_frame'

img_names = filename +".png"
matplotlib.image.imsave(img_names, img_array)
print(filename + " was saved")
plt.imshow(img_array) 