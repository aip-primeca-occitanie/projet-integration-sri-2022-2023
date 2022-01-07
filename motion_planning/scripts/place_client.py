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
# containing only the PlaceAruco class.

import rospy
import time
from motion_planning.msg import PickUpPoseAction, PickUpPoseGoal
from geometry_msgs.msg import PoseStamped, Pose
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal
from actionlib import SimpleActionClient

import tf2_ros
from tf2_geometry_msgs import do_transform_pose

import numpy as np
from std_srvs.srv import Empty

import cv2
from cv_bridge import CvBridge

from moveit_msgs.msg import MoveItErrorCodes
moveit_error_dict = {}
for name in MoveItErrorCodes.__dict__.keys():
    if not name[:1] == '_':
        code = MoveItErrorCodes.__dict__[name]
        moveit_error_dict[code] = name


class PlaceAruco():
    
    def __init__(self):
        rospy.loginfo("Initalizing...")
        self.bridge = CvBridge()
        self.tfBuffer = tf2_ros.Buffer()
        self.tf_l = tf2_ros.TransformListener(self.tfBuffer)
               
        rospy.loginfo("Waiting for /place_pose AS...")
        self.place_as = SimpleActionClient('/place_pose', PickUpPoseAction)

        self.place_as.wait_for_server()

        rospy.loginfo("Setting publishers to torso and head controller...")
        self.torso_cmd = rospy.Publisher(
            '/torso_controller/command', JointTrajectory, queue_size=1)
        self.head_cmd = rospy.Publisher(
            '/head_controller/command', JointTrajectory, queue_size=1)
        self.detected_pose_pub = rospy.Publisher('/detected_aruco_pose',
                             PoseStamped,
                             queue_size=1,
                             latch=True)

        rospy.loginfo("Waiting for '/play_motion' AS...")
        self.play_m_as = SimpleActionClient('/play_motion', PlayMotionAction)
        if not self.play_m_as.wait_for_server(rospy.Duration(20)):
            rospy.logerr("Could not connect to /play_motion AS")
            exit()
        rospy.loginfo("Connected!")
        rospy.sleep(1.0)
        rospy.loginfo("Done initializing PlaceAruco.")

    def strip_leading_slash(self, s):
        return s[1:] if s.startswith("/") else s

    def place_aruco(self, string_operation):
        #self.prepare_robot()

        # Getting the pose of the QR code
        rospy.sleep(2.0)
        rospy.loginfo("spherical_grasp_gui: Waiting for an aruco detection")
        aruco_pose = rospy.wait_for_message('/aruco_marker2/pose', PoseStamped)
        aruco_pose.header.frame_id = self.strip_leading_slash(aruco_pose.header.frame_id)
        rospy.loginfo("Got: " + str(aruco_pose))


        rospy.loginfo("spherical_grasp_gui: Transforming from frame: " +
        aruco_pose.header.frame_id + " to 'base_footprint'")
        ps = PoseStamped()
        ps.pose.position = aruco_pose.pose.position
        ps.header.stamp = self.tfBuffer.get_latest_common_time("base_footprint", aruco_pose.header.frame_id)
        ps.header.frame_id = aruco_pose.header.frame_id
        transform_ok = False
        
        while not transform_ok and not rospy.is_shutdown():
            try:
                transform = self.tfBuffer.lookup_transform("base_footprint", 
                                       ps.header.frame_id,
                                       rospy.Time(0))
                aruco_ps = do_transform_pose(ps, transform)
                transform_ok = True
            except tf2_ros.ExtrapolationException as e:
                rospy.logwarn(
                    "Exception on transforming point... trying again \n(" +
                    str(e) + ")")
                rospy.sleep(0.01)
                ps.header.stamp = self.tfBuffer.get_latest_common_time("base_footprint", aruco_pose.header.frame_id)
            place_g = PickUpPoseGoal()

        
        if string_operation == "place":
            # Raising the arm
            self.lift_torso()
            pmg = PlayMotionGoal()
            pmg.motion_name = 'preplace'
            self.play_m_as.send_goal_and_wait(pmg)
            pmg.skip_planning = False

            # Place the arm safe above table
            self.lift_torso()
            pmg = PlayMotionGoal()
            pmg.motion_name = 'pick_apporach_pose'
            self.play_m_as.send_goal_and_wait(pmg)
            pmg.skip_planning = False
			
            # Finding place position
            rospy.loginfo("Setting place position based on Perception")
            place_g.object_pose.pose.position = aruco_ps.pose.position
            place_g.object_pose.pose.position.z += 0.1*(1.0/2.0)

            rospy.loginfo("aruco pose in base_footprint:" + str(place_g))

            place_g.object_pose.header.frame_id = 'base_footprint'
            place_g.object_pose.pose.orientation.w = 1.0
            self.detected_pose_pub.publish(place_g.object_pose)
			
            rospy.loginfo("Gonna place:" + str(place_g))
            self.place_as.send_goal_and_wait(place_g)
            rospy.loginfo("Done!")

            # Move torso to its maximum height
            self.lift_torso()

            # Raise arm
            rospy.loginfo("Moving arm to a safe pose")
            pmg = PlayMotionGoal()
            pmg.motion_name = 'place_final_pose'
            pmg.skip_planning = False
            self.play_m_as.send_goal_and_wait(pmg)
            rospy.loginfo("Raising arm done.")
            
            # Place the arm safe above table
            pmg = PlayMotionGoal()
            pmg.motion_name = 'home_approach_pose'
            self.play_m_as.send_goal_and_wait(pmg)
            pmg.skip_planning = False

            # Place the object to safe navigation position
            rospy.loginfo("Going back to home position.")
            pmg = PlayMotionGoal()
            pmg.motion_name = 'home_pose'
            self.play_m_as.send_goal_and_wait(pmg)
            pmg.skip_planning = False

    def lift_torso(self):
        rospy.loginfo("Moving torso up")
        jt = JointTrajectory()
        jt.joint_names = ['torso_lift_joint']
        jtp = JointTrajectoryPoint()
        jtp.positions = [0.34]
        jtp.time_from_start = rospy.Duration(2.5)
        jt.points.append(jtp)
        self.torso_cmd.publish(jt)

    def lower_head(self):
        rospy.loginfo("Moving head down")
        jt = JointTrajectory()
        jt.joint_names = ['head_1_joint', 'head_2_joint']
        jtp = JointTrajectoryPoint()
        jtp.positions = [0.0, -0.75]
        jtp.time_from_start = rospy.Duration(2.0)
        jt.points.append(jtp)
        self.head_cmd.publish(jt)
        rospy.loginfo("Done.")

    def prepare_robot(self):
        rospy.loginfo("Unfold arm safely")
        pmg = PlayMotionGoal()
        pmg.motion_name = 'pregrasp'
        pmg.skip_planning = False
        self.play_m_as.send_goal_and_wait(pmg)
        rospy.loginfo("Done.")

        self.lower_head()

        rospy.loginfo("Robot prepared.")








