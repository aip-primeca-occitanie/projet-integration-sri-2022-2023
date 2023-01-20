#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys
import time
import os
import math

import actionlib
import actionlib_tutorials.msg
import sri_tiago_navigation.msg
import std_msgs

from std_srvs.srv import Empty

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped, PointStamped
from sri_tiago_navigation.srv import *

points = []
def callbackS1(data):
    rospy.loginfo(data)
    points.append(data)

def callbackS2(req):
    # rospy.loginfo(req)
    for point in points:
        pose = PoseStamped()
        pose.header = std_msgs.msg.Header()
        pose.header.stamp = rospy.Time.now()
        pose.header.frame_id = "map"
        pose.pose = Pose()
        pose.pose.position.x = point.point.x #  kinect Z value, [2], is X in TF of camera_link
        pose.pose.position.y = point.point.y # kinect X value, [0], is -Y in TF of camera_link
        pose.pose.position.z = 0.0 # point.z # kinect Y value, [1], is -Z in TF of camera_link
        pose.pose.orientation.x = 0.0
        pose.pose.orientation.y = 0.0
        pose.pose.orientation.z = 0.0
        pose.pose.orientation.w = 1.0
        client = actionlib.SimpleActionClient('sri_tiago_navigation_server', sri_tiago_navigation.msg.NavigationAction)

        # Waits until the action server has started up and started
        # listening for goals.
        client.wait_for_server()
        
        goal = sri_tiago_navigation.msg.NavigationGoal()

        # Creates a goal to send to the action server.
        goal.target.header.frame_id = "map"
        goal.target.pose.position = pose.pose.position
        goal.target.pose.orientation = pose.pose.orientation

        # Sends the goal to the action server.
        client.send_goal(goal)
        rospy.logerr("Sent pose")

        # Waits for the server to finish performing the action.
        client.wait_for_result()
    return []

sub_publishPoint = rospy.Subscriber('/clicked_point', PointStamped, callbackS1)

def services_loader():
    rospy.init_node('pose_estimate')
    s = rospy.Service('/sri23/estimate_pose',Empty,callbackS2)
    rospy.spin()

if __name__=="__main__":
    services_loader()
