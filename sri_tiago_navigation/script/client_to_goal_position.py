#! /usr/bin/env python

import rospy
import sys
import actionlib

import sri_tiago_navigation.msg

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion, PointStamped, PoseStamped
import math



def NavigationClient(goal):

    client = actionlib.SimpleActionClient('take_to_goal', MoveBaseAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.

    # Sends the goal to the action server.
    client.send_goal(goal) # of type PoseStamped

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  

if __name__ == '__main__':
    try:
        rospy.init_node('navigation_client')
        goal = PoseStamped()
        result = NavigationClient(goal)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)