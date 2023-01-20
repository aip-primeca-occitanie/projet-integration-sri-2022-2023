#! /usr/bin/env python

import rospy

import actionlib

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Quaternion, PointStamped
from pmb2_conveyor_control.ConveyorController import ConveyorController

class NavigationAction(object):

	def __init__(self):
		self._sub = rospy.Subscriber("/clicked_point", PointStamped, self.rviz_point)
		self._conveyorController = ConveyorController(safe_start=True)

	def rviz_point(self, msg):
		self.movebase_client(msg.point, Quaternion(0.0, 0.0, 0.0, 1.0), "map")
		self._conveyorController.activate_conveyor(3.0, 1.0, False)

	def movebase_client(self, point, quaternion, frame):
		# Create an action client called "move_base" with action definition file "MoveBaseAction"
		client = actionlib.SimpleActionClient('move_base',MoveBaseAction)

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

        
if __name__ == '__main__':
    rospy.init_node('sri_pmb2_nav_conveyor')
    server = NavigationAction()
    rospy.spin()
