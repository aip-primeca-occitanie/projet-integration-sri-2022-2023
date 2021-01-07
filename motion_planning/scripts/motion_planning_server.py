#! /usr/bin/env python

import rospy
import actionlib
import motion_planning.msg 
from geometry_msgs.msg import PoseStamped

class MotionPlanningAction(object):
	# create messages that are used to publish feedback/result
	#_feedback = actionlib_tutorials.msg.FibonacciFeedback()
	_result = motion_planning.msg.PickUpPoseResult()

	def __init__(self, name):
		self._action_name = name
		self._as = actionlib.SimpleActionServer(self._action_name, motion_planning.msg.PickUpPoseAction, execute_cb=self.execute_cb, auto_start = False)
		self._as.start()

	def execute_cb(self, goal):
		# helper variables
		r = rospy.Rate(1)
		success = True

		# publish info to the console for the user
		rospy.loginfo('%s: Executing, motion planning server ' % (self._action_name))

		# start executing the action
		pub = rospy.Publisher('/aruco_single/pose', PoseStamped, queue_size=10)
		pub.publish(goal)

		if self._as.is_preempt_requested():
			rospy.loginfo('%s: Preempted' % self._action_name)
			self._result = 1
			self._as.set_preempted(self._result)
			success = False
			return
  
		if success:
			rospy.loginfo('%s: Succeeded' % self._action_name)
			self._result = 0
			self._as.set_succeeded(self._result)

if __name__ == '__main__':
	rospy.init_node('motion_planning')
	server = MotionPlanningAction("sam_ja")
	rospy.spin()
