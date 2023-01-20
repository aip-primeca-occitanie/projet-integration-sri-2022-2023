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

from move_base_msgs.msg import MoveBaseAction, MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped, PointStamped
from sri_tiago_navigation.srv import *

points = []
def callbackS1(data):
    rospy.loginfo(data)
    points.append(data)

def callbackS2(req):
    rospy.loginfo(points)
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
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        
        client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = pose.pose
        rospy.loginfo(goal)
        
        client.send_goal(goal)
        wait = client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            pass
    return []

sub_publishPoint = rospy.Subscriber('/clicked_point', PointStamped, callbackS1)

def services_loader():
    rospy.init_node('pose_estimate')
    s = rospy.Service('/sri23/trajectory_planner',Empty,callbackS2)
    rospy.spin()

if __name__=="__main__":
    services_loader()