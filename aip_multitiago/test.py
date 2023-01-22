#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('multi_robot_controlleur', anonymous=True)
pub = rospy.Publisher('/tiago4/mobile_base_controller/cmd_vel', Twist)
message = Twist()
message.linear.x = 1
message.linear.y = 0
message.linear.z = 0
message.angular.z = 0
pub.publish(message)


while not rospy.is_shutdown():
    pub.publish(message)
    time.sleep(1)