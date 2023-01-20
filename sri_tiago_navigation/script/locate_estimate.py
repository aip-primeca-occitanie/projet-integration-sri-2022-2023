#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys
import time
import os
import math

import actionlib
import sri_tiago_navigation.msg

from std_srvs.srv import Empty

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped, PointStamped
from sri_tiago_navigation.srv import *


class locate_estimate:
    def __init__(self, nName = 'locate_estimate', sName = '/sri23/estimate_pose'):
        rospy.init_node(nName)
        self._positions = []
        rospy.Subscriber('/clicked_point', PointStamped, self.callbackT1) # subscribe to the clicked_point
        self._pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
        self._s = rospy.Service(sName, Empty, self.callbackS2)
        rospy.spin()

    def NavigationClient(goal):
        client = actionlib.SimpleActionClient('take_to_goal', MoveBaseAction)

        # Waits until the action server has started up and started
        # listening for goals.
        client.wait_for_server()

        # Sends the goal to the action server.
        client.send_goal(goal) # of type PoseStamped

        # Waits for the server to finish performing the action.
        client.wait_for_result()

    # Prints out the result of executing the action
        return client.get_result() 

    def callbackT1(self, data):
        rospy.loginfo(data)
        self._positions.append(data)

    def callbackS2(self, req):
        # rospy.loginfo(req)
        for point in self._positions:
            pose = PoseStamped()
            pose.header = point.header
            pose.header.stamp = rospy.Time.now()
            pose.header.frame_id = "map"
            pose.pose = Pose()
            pose.pose.position.x = point.point.x 
            pose.pose.position.y = point.point.y
            pose.pose.position.z = 0.0 
            pose.pose.orientation.x = 0.0
            pose.pose.orientation.y = 0.0
            pose.pose.orientation.z = 0.0
            pose.pose.orientation.w = 1.0

            goal = MoveBaseGoal()

            # Creates a goal to send to the action server.
            goal.target.header.frame_id = "map"
            goal.target.pose.position = pose.pose.position
            goal.target.pose.orientation = pose.pose.orientation

            # Sends the goal to the action server.
            result = self.NavigationClient(goal)
            rospy.logerr("Sent pose")
        return []


if __name__== "__main__":
    loc_est = locate_estimate("locate_estimate")