#!/usr/bin/env python

import rospy
import os
import sys

#start node
if __name__ == '__main__':
	rospy.init_node('update_rviz_map')
	copy_path = "scp -r " + sys.argv[1] + " tiago-88c:$HOME/.pal/tiago_maps/configurations"
	os.system(copy_path)
	os.system("rosservice call /pal_map_manager/change_map \"input: \'salle_groix\'\"")
