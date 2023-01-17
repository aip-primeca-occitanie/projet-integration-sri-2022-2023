#! /usr/bin/env python

import rospy

import rospy
from geometry_msgs.msg import Twist
import sys
import time
import os

import actionlib
import actionlib_tutorials.msg
import navigation.msg

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion

class LocalisationAction(object):
    # create messages that are used to publish feedback/result
    _result = navigation.msg.LocalisationResult()
    pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1)

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, navigation.msg.LocalisationAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()

   
    def execute_cb(self, goal):
        # helper variables
	os.system('rosservice call /global_localization \"{}\"') 
	
	# Create a Twist message and add linear x and angular z values
    	move_cmd = Twist()
    	move_cmd.angular.z = 1
       
        # publish info to the console for the user
        rospy.loginfo('Executing, localisation ')


	t0 = time.time()
	total = t0+20

    	# For the next 20 seconds publish cmd_vel move commands to Turtlesim
    	while time.time() < total:
		if self._as.is_preempt_requested():
           		rospy.loginfo('%s: Preempted' % self._action_name)
			self._result.result_code = 1;
           		self._as.set_preempted(self._result)      		
		self.pub.publish(move_cmd)
        	rospy.sleep(0.1) 

    	rospy.loginfo("Localisation test finished.")

	self._result.result_code = 0;
        self._as.set_succeeded(self._result)

        
if __name__ == '__main__':
    rospy.init_node('localisation')
    server = LocalisationAction(rospy.get_name())
    rospy.spin()
