#!/usr/bin/env python
# license removed for brevity

import rospy
import tf
import sys

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base actio
from conveyor_controller_msgs.msg import RunConveyorAction, RunConveyorGoal, RunConveyorActionGoal
import std_msgs
import actionlib_msgs

# 
RUN_CONVEYOR_GOAL_TOPIC_NAME = "/run_conveyor/goal"

class ConveyorController():

    def __init__(self, safe_start=False, safe_sleep=0.4):
        self.pub = rospy.Publisher(RUN_CONVEYOR_GOAL_TOPIC_NAME, RunConveyorActionGoal, queue_size=1)
        if safe_start:
            rospy.sleep(safe_sleep)

    def activate_convoyer(self, duration_seconds, speed, reverse):
        """
        Enable the conveyor belt:
            - duration_seconds: duration in seconds
            - speed: speed
            - reverse: direction (False: torwards the robot's direction, True: backwards)
        """

        # Create the message to be sent on the topic through a publisher (and not as an Action)
        msg = RunConveyorActionGoal()

        # Setup header and goalId
        msg.header = std_msgs.msg.Header()
        msg.goal_id = actionlib_msgs.msg.GoalID()

        # Setup the current conveyor control information
        msg.goal = RunConveyorGoal()
        msg.goal.duration = std_msgs.msg.Duration(rospy.Duration.from_sec(duration_seconds))
        msg.goal.speed = speed
        msg.goal.reverse = reverse

        self.pub.publish(msg)

        rospy.loginfo("Conveyor control message sent")
