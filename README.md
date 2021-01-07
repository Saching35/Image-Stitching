# ComputerVision

How to run SIFTImageStitching.py
1. Place SIFTImageStitching.py file and Images folder together
2. Install opencv-contrib-python=3.4.2.16 into python
3. Run .py file by using Python Compiler

How to run OpenCVImageStitching.py
1. Place SIFTImageStitching.py file and Images folder together
2. Install opencv=4.0.1 into python
3. Run .py file by using Python3 Compiler





# Image Stitching using SIFT

1. The Images are read and the converted into grayscale form
2. Using SIFT, keypoints and descriptors for the both images are calculated
3. A kNN matcher is used to match descriptors from the both the images. A value of k is set to 2 which gives us 2 best matches for every descriptor
4. Distance between every descriptor in first image and every descriptor in second image is calculated and top matches are selected
5. With the help of ratio test, using RANSAC, homography is calculated
6. drawMatches is used to show matched keypoints
7. Using warpPerspective, images are aligned together and then stiched
8. The empty black part from the image is removed



Note - SIFT has been removed from the opencv module from version > 3.4.2



# Image Stitching using OpenCV stitcher

To stitch these 2 images, I have used stitcher module from opencv.
Following steps are performed while stitching images
  1. Resize - Images are resized to medium resolution
  2. Features are searched and stored for each image
  3. Features from different images are mapped together
  4. If enough amount of features are mapped then images are stitched together and then warped to create warped image