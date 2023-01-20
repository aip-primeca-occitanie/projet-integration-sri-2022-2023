#! /usr/bin/env python
from __future__ import print_function
import rospy

# Brings in the SimpleActionClient
import actionlib
import sys

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import actionlib_tutorials.msg
import sri_tiago_navigation.msg
from geometry_msgs.msg import Pose, Point, Quaternion

def navigation_client(point, quaternion, frame):
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('sri_tiago_navigation_server', sri_tiago_navigation.msg.NavigationAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()
	
    goal = sri_tiago_navigation.msg.NavigationGoal()

    # Creates a goal to send to the action server.
    goal.target.header.frame_id = frame;
    goal.target.pose.position = point;
    goal.target.pose.orientation = quaternion;

    # Sends the goal to the action server.
    client.send_goal(goal)
    rospy.logerr("Sent pose")

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('sri_tiago_navigation_client_py')
        locations = {
            "milieu": {
                "point": Point(0.863, -0.608, 0),
                "quaternion": Quaternion(0.0, 0.0, -0.183, 0.983),
                "frame": "map"
            },
            "milieu-test": {
                "point": Point(-0.346, -2.286, 0),
                "quaternion": Quaternion(0.0, 0.0, 0.871, -0.871),
                "frame": "map"
            },
            "init-42": {
                "point": Point(1.500, -4.399, 0),
                "quaternion": Quaternion(0.0, 0.0, 0.791, 0.610),
                "frame": "map"
            },
            "end-42": {
                "point": Point(4.870, -10.777, 0),
                "quaternion": Quaternion(0.0, 0.0, 0.996, -0.086),
                "frame": "map"
            }
        }

        locationName = sys.argv[1]
        location = locations[locationName]

        result = navigation_client(location["point"], location["quaternion"], location["frame"])
        print(result)
        print("Result: ", result.result_code)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
