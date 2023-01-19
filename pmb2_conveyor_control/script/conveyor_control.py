#!/usr/bin/env python

import rospy
import tf
import sys

from pmb2_conveyor_control.ConveyorController import ConveyorController

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Not enough arguments")
        print("Usage: rosrun pmb2_conveyor_control <duration> <speed> <reverse:True|False>")
        exit(1)

    duration_seconds = float(sys.argv[1])
    speed = float(sys.argv[2])
    reverse = sys.argv[3].lower() == "true"

    conveyorController = ConveyorController(safe_start=True)

    conveyorController.activate_convoyer(duration_seconds, speed, reverse)

    rospy.loginfo("Conveyor execution done!")
