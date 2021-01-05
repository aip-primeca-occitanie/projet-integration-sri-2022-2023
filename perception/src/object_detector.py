#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped
from cv_bridge import CvBridge
import cv2
import math
import numpy as np

def color_based_detection(inputImage):
    npInputimage = inputImage.copy()
    npBlurredInputImage = cv2.GaussianBlur(npInputimage, (31, 31), 0)
    # color segmentation boundaries  
    #lower, upper = [51, 0, 102], [100, 51, 200] #sac
    #lower, upper = [0, 153, 112], [128, 255,221 ] # boule verte
    iLower, iUpper = [40, 32, 104], [110, 75,255 ] # boule rouge
   
    # Create NumPy arrays from the boundaries
    iLower, iUpper = np.array(iLower, dtype = "uint8"), np.array(iUpper, dtype = "uint8")
    
    # Segment the object defined by the colors within the given boundaries 
    npSegmentedImage = cv2.inRange(npBlurredInputImage, iLower, iUpper)
    
    #reconstruct the the rgb color of the segmented target 
    npReconstucted_RGBImage = cv2.bitwise_and(inputImage, inputImage, mask = npSegmentedImage)
    return npReconstucted_RGBImage

def showImage(cvIamge):
    """
    Show an OpenCV image on the screen. 
    Args : 
    cvIamge = OpenCV image
    Output :
    show an image with OpenCV
    """
    cv2.imshow('image', cvIamge)
    cv2.waitKey(1)

