#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from skimage import color, io
import matplotlib.pyplot as plt


# In[4]:


img1 = cv2.imread('./Images/pan1.jpg')#reading image 1
img2 = cv2.imread('./Images/pan2.jpg')#reading image 2
finalimg = []
finalimg.append(img1)
finalimg.append(img2)
stitcher = cv2.Stitcher.create()#creating stitcher using cv2


result = stitcher.stitch(finalimg)#stitching both images

plt.imshow(result[1])
plt.show()
cv2.imwrite("./Images/pano.jpg", result[1])


# In[ ]:




