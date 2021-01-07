#!/usr/bin/env python
# license removed for brevity

import rospy
import tf
import sys

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion

def movebase_client(point, quaternion, frame):

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

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    print(sys.argv)
    if sys.argv[1] == "depart":
      point = Point(-3.47, 5.57, 0)
      quaternion = Quaternion(0.0, 0.0, -3.5, 0.77)
      frame = "map"
    if sys.argv[1] == "prise":
      point = Point(target.point)
      quaternion = Quaternion(target.quaternion)
    if sys.argv[1] == "depose":
      point = Point(-0.47, 0.45, 0)
      quaternion = Quaternion(0.0, 0.0, 0.5, 0.77)
      frame= "map"
    if sys.argv[1] == "approche":
      point = Point(0.1, 0.0, 0)
      quaternion = Quaternion(0.0, 0.0, 0.0, 0.77)
      frame= "base_footprint"

    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client(point, quaternion, frame)
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
