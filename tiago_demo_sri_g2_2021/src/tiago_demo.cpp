#include "ros/ros.h"
#include <actionlib/server/simple_action_server.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <tiago_demo_sri_g2_2021/PickUpPoseAction.h>
#include <tiago_demo_sri_g2_2021/NavigationAction.h>
#include <string>


enum State {IDLE, PICK, PLACE, MOVING_PICK, MOVING_PLACE, DONE, FAIL};
State currentState = IDLE;
bool navServerBusy = false;
bool pupServerBusy = false;

//liste des etat :
//FAIL = 1;
//MOVE_PICK = 2;
//MOVE_PLACE = 3;
//PICK = 4;
//PLACE = 5;
//DONE = 6
//IDLE = 7;

void navigationCallback(const tiago_demo_sri_g2_2021::NavigationActionResultConstPtr& resultat) 
{
	int resultVal = resultat->result.result_code;
  switch (resultVal)
	{
		case 0 :
			if (currentState == MOVING_PICK)
			{
				currentState = PICK;
			}
			if (currentState == MOVING_PLACE)
			{
				currentState = PLACE;
			}
			break;


		case 1 :
			currentState = FAIL;
			break;
	}
	navServerBusy = false;			
}

void pickUpPoseCallback(const tiago_demo_sri_g2_2021::PickUpPoseActionResultConstPtr& resultat) 
{
	int resultVal = resultat->result.result_code;
  switch (resultVal)
	{
		case 0 :
			if (currentState == PICK)
			{
				currentState = MOVING_PLACE;
			}
			if (currentState == PLACE)
			{
				currentState = DONE;
			}
			break;


		case 1 :
			currentState = FAIL;
			break;
	}	

	pupServerBusy = false;		
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "demo");

  ros::NodeHandle n;
	
	tiago_demo_sri_g2_2021::PickUpPoseGoal pickPlaceGoal;
  pickPlaceGoal.item_target.header.frame_id = "head";
  pickPlaceGoal.item_target.point.x = 20.0;
  pickPlaceGoal.item_target.point.y = 0.0;
  pickPlaceGoal.item_target.point.z = -25.0;

	tiago_demo_sri_g2_2021::NavigationGoal navGoalPick;
  navGoalPick.target.header.frame_id = "baselink";
  navGoalPick.target.pose.position.x = 20.0;
  navGoalPick.target.pose.position.y = 85.0;
  navGoalPick.target.pose.position.z = 0.0;
  navGoalPick.target.pose.orientation.x = 1.0;
  navGoalPick.target.pose.orientation.y = 2.0;
  navGoalPick.target.pose.orientation.z = 0.0;
  navGoalPick.target.pose.orientation.w = 1.0;

	tiago_demo_sri_g2_2021::NavigationGoal navGoalPlace;
  navGoalPlace.target.header.frame_id = "baselink";
  navGoalPlace.target.pose.position.x = 0.0;
  navGoalPlace.target.pose.position.y = 0.0;
  navGoalPlace.target.pose.position.z = 0.0;
  navGoalPlace.target.pose.orientation.x = 2.0;
  navGoalPlace.target.pose.orientation.y = 1.0;
  navGoalPlace.target.pose.orientation.z = 0.0;
  navGoalPlace.target.pose.orientation.w = 1.0;

	// create the pickUpPose action client
  // true causes the client to spin its own thread
  actionlib::SimpleActionClient<tiago_demo_sri_g2_2021::PickUpPoseAction> pupac("pickuppose", true);

  // create the navigation action client
  // true causes the client to spin its own thread
  actionlib::SimpleActionClient<tiago_demo_sri_g2_2021::NavigationAction> navac("navigation", true);

	ROS_INFO("Waiting for pickUpPose action server to start.");
  // wait for the pickUpPose action server to start
  pupac.waitForServer(); //will wait for infinite time

	ROS_INFO("Waiting for navigation action server to start.");
  // wait for the pickUpPose action server to start
  navac.waitForServer(); //will wait for infinite time

	ros::Subscriber pupsub = n.subscribe("/pickuppose/result", 1000, pickUpPoseCallback);		
	ros::Subscriber navsub = n.subscribe("/navigation/result", 1000, navigationCallback);
	

  ros::Rate loop_rate(10);
  while (ros::ok())
  {

		switch (currentState)
		{
			case IDLE:
				currentState = MOVING_PICK;
				break;

			case MOVING_PICK:
				if (!navServerBusy)
				{
					navac.sendGoal(navGoalPick);
					navServerBusy = true;
				}
				break;

			case MOVING_PLACE:
					if (!navServerBusy)
					{
						navac.sendGoal(navGoalPlace);
						navServerBusy = true;
					}
					break;

			case PLACE:
				if (!pupServerBusy)
				{
					pupac.sendGoal(pickPlaceGoal);
					pupServerBusy = true;
				}
				break;

			case PICK:
				if (!pupServerBusy)
				{
					pupac.sendGoal(pickPlaceGoal);
					pupServerBusy = true;
				}
				break;

			case FAIL:
				ROS_INFO("DEMO FAILLED...RETRY");
				return 0;
				break;

			case DONE:
				ROS_INFO("DEMO SUCCEDED...GG");
				return 0;
				break;

			default:
				ROS_INFO("PAS DE currentState SPECIFIE... NUL....");
				return 0;
				break;
	}
		
				


    ros::spinOnce();

    loop_rate.sleep();
  }

  return 0;
}
