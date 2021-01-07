import numpy as np
import cv2
import matplotlib.pyplot as plt


# Ref: https://towardsdatascience.com/image-stitching-using-opencv-817779c86a83
# Reading 2 Images
img_ = cv2.imread("./Images/hogleft.jpg")
img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)
img = cv2.imread("./Images/hogright.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.imshow(img1)
plt.show()
plt.imshow(img2)
plt.show()

# creating sift object
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)


# Create brute force matcher
bf = cv2.BFMatcher()

# Using brute force matcher on descriptors
matches = bf.knnMatch(des1,des2, 2)

# Applying ratio test
good = []
for m,n in matches:
    if m.distance < n.distance * 0.5:
        good.append(m)

if len(good) >= 10:
    src = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
    #print H
else:
    raise AssertionError("Cannot find enough keypoints.")
    
    
    
    
# Drawing Features    
draw_params = dict(matchColor = (0,255,0), singlePointColor = None, flags = 2)

# Draw first 10 matches.
match_img = cv2.drawMatches(img_, kp1, img, kp2, good, None, **draw_params)

# convert and save image
match_img = cv2.cvtColor(match_img, cv2.COLOR_BGR2RGB)
plt.imshow(match_img)
plt.show()
    
# warp two images together
Hinv = np.linalg.inv(H)  

dst = cv2.warpPerspective(img,Hinv,(img.shape[1]+img_.shape[1], img.shape[0]))
plt.imshow(dst)
plt.show()
dst[0:img_.shape[0], 0:img_.shape[1]] = img_
cv2.imwrite("output.jpg",dst)
plt.imshow(dst)
plt.show()


# Removeing Extra black part of the image

h, w = dst.shape[:2]
gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
first_pass = True
pixels = np.sum(gray, axis=0).tolist()

# Build new image
for index, value in enumerate(pixels):
    if value == 0:
        continue
    else:
        ROI = dst[0:h, index:index+1]
        if first_pass:
            resultfinal = dst[0:h, index+1:index+2]
            first_pass = False
            continue
        resultfinal = np.concatenate((resultfinal, ROI), axis=1)

plt.imshow(resultfinal)
plt.show()
cv2.imwrite('./Images/resultfinal.png', resultfinal)





