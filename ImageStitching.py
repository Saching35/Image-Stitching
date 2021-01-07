#!/usr/bin/env python
# coding: utf-8

# In[12]:


import cv2
import numpy as np
from skimage import color, io
import matplotlib.pyplot as plt


# In[16]:


img1 = cv2.imread('./Images/pan1.jpeg')#reading image 1
img2 = cv2.imread('./Images/pan2.jpeg')#reading image 2
finalimg = []
finalimg.append(img1)
finalimg.append(img2)
stitcher = cv2.Stitcher.create()#creating stitcher using cv2


result = stitcher.stitch(finalimg)#stitching both images

cv2.imwrite("./Images/pano.jpg", result[1])


# In[ ]:




