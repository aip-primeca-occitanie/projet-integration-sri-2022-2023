#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped
from cv_bridge import CvBridge
import cv2
import math
import numpy as np
global iX_target, iY_target,fPreviousDepth
iX_target = 0 
iY_target = 0
fPreviousDepth = 0

def template_matching_detection(inputImage):
    global iX_target, iY_target
    npInputimage = np.copy(inputImage)
    npSegmentedInputimage = color_based_detection(npInputimage)
    #print(np.shape(npInputimage))
    npBlurredInputImage = cv2.GaussianBlur(npSegmentedInputimage, (79, 79), 0)
    npTemplate = cv2.imread('/home/etudiant/ros_integration_ws/src/projet-integration-sri-2020-2021/perception/scripts/cube.png') 
    npSegmentedTemplate = color_based_detection(npTemplate)

    # Application of the normalized correlation
    npCorrelatedImage = cv2.matchTemplate(npBlurredInputImage[:,:,1],npSegmentedTemplate[:,:,1],cv2.TM_CCORR_NORMED)
    #print(np.shape(npCorrelatedImage))

    iMin_val, iMax_val, iMin_loc, iMax_loc = cv2.minMaxLoc(npCorrelatedImage)

    #print("val {}".format(iMax_val))
  
    #Drawing the bounding box
    if(iMax_val>0.5):
        iX_target = iMax_loc[0] + np.shape(npTemplate)[0]//2 
        iY_target = iMax_loc[1] + np.shape(npTemplate)[1]//2
        cv2.circle(npSegmentedInputimage,(iX_target,iY_target),1,255,thickness=2)
        cv2.rectangle(npSegmentedInputimage,(iMax_loc[0],iMax_loc[1]),((iMax_loc[0]+np.shape(npTemplate)[1]) ,(iMax_loc[1]+np.shape(npTemplate)[0])),255,thickness=2)
        cv2.putText(npSegmentedInputimage,"Cube", (iMax_loc[0],iMax_loc[1]-10), cv2.FONT_HERSHEY_DUPLEX, 1, 100,thickness=2)
        
    demo(inputImage,npSegmentedInputimage)
    return iX_target, iY_target

def demo(inputImage, outputImage):
    cv2.imshow("images", np.hstack([inputImage, outputImage]))
    cv2.waitKey(1)


def color_based_detection(inputImage):
    npInputimage = np.copy(inputImage)
    npBlurredInputImage = cv2.GaussianBlur(npInputimage, (31, 31), 0)
    # color segmentation boundaries  
    #lower, upper = [51, 0, 102], [100, 51, 200] #sac
    #lower, upper = [0, 153, 112], [128, 255,221 ] # boule verte
    ###iLower, iUpper = [40, 32, 104], [110, 75,255 ] # boule rouge
    iLower, iUpper = [1, 101, 2], [100, 255,100 ] # cube vert test simulation
   
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

def process_image(smiMsg):
    """
    Convert a Sensor message image (RBG) from ROS to an OpenCV image. 
    Then apply some usefull functions to this new image. 
    It will publish on the target_point_into_image topic the target position in a PoseStamped format. 
    Args : 
    smiMsg = sensor message image which represents the rgb image from the camera
    Output :
    nothing, it just calls functions 
    """
    try:
        # convert sensor_msgs/Image to OpenCV Image
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(smiMsg, "bgr8")
        cvDrawImg = orig

    except Exception as err:
        print(err)

    # show the image 
    #rospy.sleep(1)
    #showImage(cvDrawImg)
    
    # find the position of the target in the image plan 
    color_based_detection(cvDrawImg)
    ix,iy = template_matching_detection(cvDrawImg) # image frame

    fz = getDepth(iy,ix) # openCV and the realsense depth don't use the same x and y

    # publish in the target_point topic 
    pub = rospy.Publisher('target_point_into_image', PointStamped, queue_size=10)

    psGoal = PointStamped()
    psGoal.header.stamp = rospy.get_rostime()
    psGoal.header.frame_id = "camera_color_optical_frame"
    psGoal.point.x = ix
    psGoal.point.y = iy
    psGoal.point.z = fz
    rospy.loginfo(psGoal)
    pub.publish(psGoal)

def getDepth(ix,iy):
    """
    Get the value of the depth with a position (x,y) in the image. 
    The value is computed by applying the median filter idea and a mean. It helps to remove high pic of noise and small noise. 
    Args : 
    ix = the x position of a point in the image
    iy = the y position of a point in the image
    Output :  
    fMean = the depth of the (x,y) point
    """
    lfNeighboors = []
    for i in range(-1,2):
        for j in range(-1,2):
            lfNeighboors.append(naDepth_array[ix+i][iy+j])
        
    sorted(lfNeighboors)
    # remove higher and lower value to reduce potential noise
    lSub_neighboors = lfNeighboors[1:8]
    # compute the mean of neighboors
    fMean = np.mean(lSub_neighboors)

    if fMean > 0.0:
        global fPreviousDepth
        fPreviousDepth = fMean
        return fMean

    return fPreviousDepth

def start_node():
    """
    Initialise the node and subscribe to topic. 
    Args : 
    void
    Output :
    nothing
    """
    # initialisation the node 
    rospy.init_node('main_detect')
    rospy.loginfo('main_detect node started')
    # subscribe to topics 
    rospy.Subscriber("/xtion/rgb/image_color", Image, process_image)
    rospy.Subscriber("/xtion/depth_registered/image_raw", Image, process_image_depth)

    rospy.spin()

def process_image_depth(smiMsg):
    """
    Convert a Sensor message image (depth) from ROS to a numpy array image and save the result in the naDepth_array variable

    Args : 
    smiMsg = sensor message image which represents the depth image from the camera

    Output :
    nothing 
    """
    try:
        # convert sensor_msgs/Image to OpenCV Image
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(smiMsg, "passthrough")
        # convert the OpenCV Image in a bumpy array
        global naDepth_array 
        naDepth_array = np.array(orig, dtype=np.uint16) * 0.001
        cvDrawImg = orig

    except Exception as err:
        print(err)

    # show the image 
    #showImage(cvDrawImg)
    #getDepth(naDepth_array)


if __name__ == '__main__':
    try:
        # run the main program to start the node
        start_node()
    except rospy.ROSInterruptException:
        pass

