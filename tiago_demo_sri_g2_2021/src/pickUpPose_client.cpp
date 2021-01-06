#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <tiago_demo_sri_g2_2021/PickUpPoseAction.h>

int main (int argc, char **argv)
{
  ros::init(argc, argv, "pickuppose_client");

  // create the action client
  // true causes the client to spin its own thread
  actionlib::SimpleActionClient<tiago_demo_sri_g2_2021::PickUpPoseAction> ac("pickuppose", true);

  ROS_INFO("Waiting for action server to start.");
  // wait for the action server to start
  ac.waitForServer(); //will wait for infinite time

  ROS_INFO("Action server started, sending goal.");
  // send a goal to the action
  tiago_demo_sri_g2_2021::PickUpPoseGoal goal;
  goal.item_target.header.frame_id = "head";
  goal.item_target.point.x = 0.0;
  goal.item_target.point.y = 0.0;
  goal.item_target.point.z = 0.0;
  ac.sendGoal(goal);

  //wait for the action to return
  bool finished_before_timeout = ac.waitForResult(ros::Duration(30.0));

  if (finished_before_timeout)
  {
    actionlib::SimpleClientGoalState state = ac.getState();
    ROS_INFO("Action finished: %s",state.toString().c_str());
  }
  else
    ROS_INFO("Action did not finish before the time out.");

  //exit
  return 0;
}
