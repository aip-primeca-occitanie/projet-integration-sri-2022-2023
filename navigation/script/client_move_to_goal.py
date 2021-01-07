#! /usr/bin/env python
from __future__ import print_function
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import actionlib_tutorials.msg
import navigation.msg

def navigation_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('navigation', navigation.msg.NavigationAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()
	
    goal = navigation.msg.NavigationGoal()

    # Creates a goal to send to the action server.
    goal.target.header.frame_id = "map";
    goal.target.pose.position.x = 0;
    goal.target.pose.position.y = 0;
    goal.target.pose.position.z = 0.0;
    goal.target.pose.orientation.x = 0.0;
    goal.target.pose.orientation.y = 0.0;
    goal.target.pose.orientation.z = 0.0;
    goal.target.pose.orientation.w = 1.0;

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('navigation_client_py')
        result = navigation_client()
        print("Result: ", result.result_code)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
