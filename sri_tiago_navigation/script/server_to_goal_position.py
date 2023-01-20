#! /usr/bin/env python

import rospy
import actionlib

import sri_tiago_navigation.msg

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult
from geometry_msgs.msg import Pose, Point, Quaternion, PointStamped, PoseStamped
import math


# action server to lead to a goal position 

class NavigateToGoal:
    # create messages that are used to publish feedback/result
    _result = MoveBaseResult()
    _currentPose = Pose()
    

    def __init__(self, nName, aName = 'navigate_to_goal'):
        rospy.init_node(aName)
        self._action_name = nName
        self._as = actionlib.SimpleActionServer(self._action_name, MoveBaseAction, execute_cb=self.execute_cb, auto_start = False) # action to lead to goal
        self._as.start()
        self._pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1) # topic to publish the goals
        self._eps = 1.0 # error on position tolerance
        
    def callbackT(self, data):
        rospy.loginfo(data)
        self._currentPose = data.pose  # of type PoseStamped 

    def execute_cb(self, goal):
        # helper variables
        self._pub.publish(goal)

        r = rospy.Rate(1)

        success = True
        rospy.Subscriber('/current_position?', PointStamped, self.callbackT) # find the topic of the current position
        
        # publish info to the console for the user
        rospy.loginfo('Moving robot to target position...')
        goalPosition = goal.pose.position
        err = math.sqrt((goalPosition.x - self._currentPose.position.x)**2\
            +(goalPosition.y - self._currentPose.position.y)**2\
                +(goalPosition.z - self._currentPose.position.z)**2)
        # start executing the action
        while  err > self._eps:
            # check that preempt has not been requested by the client
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
                break
            rospy.Subscriber('/current_position?', PointStamped, self.callback)
            err = math.sqrt((goalPosition.x - self._currentPose.position.x)**2\
            +(goalPosition.y - self._currentPose.position.y)**2\
                +(goalPosition.z - self._currentPose.position.z)**2)
            #self._feedback = err # current error on positionning
            # publish the feedback
            #self._as.publish_feedback(self._feedback)
            # this step is not necessary, the sequence is computed at 1 Hz for demonstration purposes
            r.sleep()
          
        if success:
            self._result = self._currentPose
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._result)
        
if __name__ == '__main__':
    server = NavigateToGoal('take_to_goal') # action name 
    rospy.spin()