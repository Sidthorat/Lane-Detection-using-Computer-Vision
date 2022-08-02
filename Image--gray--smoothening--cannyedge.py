# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:23:07 2022

@author: siddh
"""

# import opencv
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image
image = cv2.imread("C:/Users/siddh/OneDrive/Pictures/Screenshots/Documents/test_image.jpg")
cv2.imshow('Original', image)
cv2.waitKey(0)

# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

# Use the smoothening gaussian blur to the grayscale image
gray=gray_image
blur=cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow('blurred', blur)
cv2.waitKey(0)

#use the canny edge detection for right intensity detection
#derivative(f(x,y))---lRGE CHANGE====LARGE DERIVATIVE
#CV2.CANNY(IMAGE,LOW_THRESHOLD,HIGH_THRESHOLD)
canny=gray
cannyedge=cv2.Canny(canny, 50, 100)
cv2.imshow('canny edge detection', cannyedge)
cv2.waitKey(0)
# Window shown waits for any key pressing event
cv2.destroyAllWindows()


