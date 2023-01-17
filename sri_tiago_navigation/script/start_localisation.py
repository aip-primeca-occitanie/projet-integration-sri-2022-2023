#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys
import time
import os

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    # Initializes a rospy node to let the SimpleActionClient publish and subscribe
    rospy.init_node('start_localisation')
    # Create a publisher which can "talk" to Turtlesim and tell it to move
    pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1)

    os.system('rosservice call /global_localization \"{}\"')

    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()
    move_cmd.angular.z = 0.4

    # Save current time and set publish rate at 10 Hz
    t0 = time.time()

    total = t0+10

    # For the next 6 seconds publish cmd_vel move commands to Turtlesim
    while time.time() < total:
        pub.publish(move_cmd)
        rospy.sleep(0.1) 

    rospy.loginfo("Localisation test finished.")