#! /usr/bin/env python
# -*- coding: utf-8 -*-



import rospy

from sensor_msgs.msg import JointState

from std_msgs.msg import Bool



def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "Entendu : %s", data.effort[7])
	if ( data.effort[7] < -0.25):
		isGripped = True # on a la balle
	else:
		isGripped = False

	pub = rospy.Publisher('node_prise', Bool, queue_size=10)

	rospy.loginfo(isGripped)
	pub.publish(isGripped)



def start_node():
	"""
	Initialise the node and subscribe to topic. 
	"""
	# initialisation the node 
	rospy.init_node('node_prise')
	rospy.loginfo('node_prise node started')
	# subscribe to topic
	rospy.Subscriber("joint_states", JointState, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		start_node()
	except rospy.ROSInterruptException:
		pass
