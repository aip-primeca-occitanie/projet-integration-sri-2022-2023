#! /usr/bin/env python

import rospy

import actionlib

import actionlib_tutorials.msg
import navigation.msg

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion

class NavigationAction(object):
    # create messages that are used to publish feedback/result
    _feedback = navigation.msg.NavigationActionFeedback()
    _result = navigation.msg.NavigationResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, navigation.msg.NavigationAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
      
    def movebase_client(self, point, quaternion, frame):

   	# Create an action client called "move_base" with action definition file "MoveBaseAction"
    	client = actionlib.SimpleActionClient('/sri22/move_base',MoveBaseAction)
 
   	# Waits until the action server has started up and started listening for goals.
    	client.wait_for_server()

   	# Creates a new goal with the MoveBaseGoal constructor
   	goal = MoveBaseGoal()
    	goal.target_pose.header.frame_id = frame
   	goal.target_pose.header.stamp = rospy.Time.now()
   	# Move accordingly to the "robot" coordinate frame 
    	goal.target_pose.pose = Pose(point, quaternion)

   	# Sends the goal to the action server.
    	client.send_goal(goal)
   	# Waits for the server to finish performing the action.
    	wait = client.wait_for_result()
   	# If the result doesn't arrive, assume the Server is not available
    	if not wait:
        	rospy.logerr("Action server not available!")
        	rospy.signal_shutdown("Action server not available!")
    	else:
    	# Result of executing the action
        	return client.get_result()
   
    def execute_cb(self, goal):
        # helper variables
        r = rospy.Rate(1)
        success = True

	frameid = goal.target.header.frame_id	
	point = Point(goal.target.pose.position.x, goal.target.pose.position.y, goal.target.pose.position.z)
        orientation = Quaternion(goal.target.pose.orientation.x , goal.target.pose.orientation.y, goal.target.pose.orientation.z , goal.target.pose.orientation.w)     

        
        # publish info to the console for the user
        rospy.loginfo('Executing, creating navigation ')

        if self._as.is_preempt_requested():
           rospy.loginfo('%s: Preempted' % self._action_name)
	   self._result.result_code = 1;
           self._as.set_preempted(self._result)
      	   success = False
	
	result = self.movebase_client(point, orientation, frameid )
        if result:
            rospy.loginfo("Goal execution done!")
	
	self._result.result_code = 0;
        self._as.set_succeeded(self._result)

        
if __name__ == '__main__':
    rospy.init_node('navigation')
    server = NavigationAction(rospy.get_name())
    rospy.spin()
