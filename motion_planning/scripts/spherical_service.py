#!/usr/bin/env python

# Copyright (c) 2016 PAL Robotics SL. All Rights Reserved
#
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted, provided that the
# above copyright notice and this permission notice appear in all
# copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Author:
#   * Sam Pfeiffer
#   * Job van Dieten
#   * Jordi Pages
#
# This document is a modified version of the original pick_client.py 
# containing only the SphericalService class and the main.


import rospy

import pick_client
import place_client

import numpy as np
from std_srvs.srv import Empty

from moveit_msgs.msg import MoveItErrorCodes
moveit_error_dict = {}
for name in MoveItErrorCodes.__dict__.keys():
    if not name[:1] == '_':
        code = MoveItErrorCodes.__dict__[name]
        moveit_error_dict[code] = name



class SphericalService(object):
    def __init__(self):
        rospy.loginfo("Starting Spherical Grab Service")
        self.pick_type = pick_client.PickAruco()
        self.place_type = place_client.PlaceAruco()
        rospy.loginfo("Finished SphericalService constructor")
        self.place_gui = rospy.Service("/place_gui", Empty, self.start_aruco_place)
        self.pick_gui = rospy.Service("/pick_gui", Empty, self.start_aruco_pick)

    def start_aruco_pick(self, req):
        self.pick_type.pick_aruco("pick")
        return {}

    def start_aruco_place(self, req):
        self.place_type.place_aruco("place")
        return {}



if __name__ == '__main__':
    rospy.init_node('pick_aruco_demo')
    sphere = SphericalService()
    rospy.spin()
