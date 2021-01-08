#!/usr/bin/env python

import rospy
import os

#start node
if __name__ == '__main__':
	rospy.init_node('update_rviz_map')
	copy_path = "cp " + args[1] + " $HOME/.pal/tiago_maps/configurations"
	os.system(copy_path)
	os.system("rosservice call /pal_map_manager/change_map \"input: \'salle_groix\'\"")