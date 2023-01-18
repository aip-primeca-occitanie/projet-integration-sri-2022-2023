#include "ros/ros.h"
#include <actionlib/server/simple_action_server.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <tiago_demo_sri_g2_2021/PickUpPoseAction.h>
#include <sri_tiago_navigation/NavigationAction.h>
#include <sri_tiago_navigation/LocalisationAction.h>
#include <string>
#include <std_msgs/Int32.h>


enum State {IDLE, PICK, PLACE, MOVING_PICK, MOVING_PLACE, DONE, FAIL, PERCEPTION, LOCALISATION};
State currentState = IDLE;
bool navServerBusy = false;
bool pupServerBusy = false;
bool perceptionServerBusy = false;
bool locServerBusy = false;

void navigationCallback(const sri_tiago_navigation::NavigationActionResultConstPtr& resultat) 
{
	int resultVal = resultat->result.result_code;
  switch (resultVal)
	{
		case 0 :
			if (currentState == MOVING_PICK)
			{
				currentState = PERCEPTION;
			}
			if (currentState == MOVING_PLACE)
			{
				currentState = PLACE;
			}
			ROS_INFO("Fin de la tache de NAVIGATION");
			break;


		case 1 :
			currentState = FAIL;
			break;
	}
	navServerBusy = false;			
}

void localisationCallback(const sri_tiago_navigation::LocalisationActionResultConstPtr& resultat) 
{
	int resultVal = resultat->result.result_code;
  switch (resultVal)
	{
		case 0 :
			currentState = MOVING_PICK;
			ROS_INFO("Fin de la tache de LOCALISATION");
			break;

		case 1 :
			currentState = FAIL;
			break;
	}
	locServerBusy = false;			
}

void perceptionCallback(const std_msgs::Int32ConstPtr& resultat) 
{
	int resultVal = resultat->data;
  switch (resultVal)
	{
		case 0 :
			currentState = PICK;
			ROS_INFO("Fin de la tache de PERCEPTION");
			break;


		case 1 :
			currentState = FAIL;
			break;
	}
	perceptionServerBusy = false;			
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
			ROS_INFO("Fin de la tache de PICKANDPLACE");
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

	sri_tiago_navigation::NavigationGoal navGoalPick;
  navGoalPick.target.header.frame_id = "map";
  navGoalPick.target.pose.position.x = -3.75;
  navGoalPick.target.pose.position.y = 3.6;
  navGoalPick.target.pose.position.z = 0.0;
  navGoalPick.target.pose.orientation.x = 0.0;
  navGoalPick.target.pose.orientation.y = 0.0;
  navGoalPick.target.pose.orientation.z = 0.0;
  navGoalPick.target.pose.orientation.w = 1.0;

	sri_tiago_navigation::NavigationGoal navGoalPlace;
	navGoalPlace.target.header.frame_id = "map";
  navGoalPlace.target.pose.position.x = -2.3;
  navGoalPlace.target.pose.position.y = 6.39;
  navGoalPlace.target.pose.position.z = 0.0;
  navGoalPlace.target.pose.orientation.x = 0.0;
  navGoalPlace.target.pose.orientation.y = 0.0;
  navGoalPlace.target.pose.orientation.z = 0.0;
  navGoalPlace.target.pose.orientation.w = 1.0;

	sri_tiago_navigation::LocalisationGoal locGoal;
  locGoal.target = 0;

	// create the pickUpPose action client
  // true causes the client to spin its own thread
  actionlib::SimpleActionClient<tiago_demo_sri_g2_2021::PickUpPoseAction> pupac("pickuppose", true);

	// true causes the client to spin its own thread
  actionlib::SimpleActionClient<sri_tiago_navigation::LocalisationAction> locac("localisation", true);

  // create the navigation action client
  // true causes the client to spin its own thread
  actionlib::SimpleActionClient<sri_tiago_navigation::NavigationAction> navac("navigation", true);

	ROS_INFO("Waiting for pickUpPose action server to start.");
  // wait for the pickUpPose action server to start
  pupac.waitForServer(); //will wait for infinite time

	ROS_INFO("Waiting for navigation action server to start.");
  // wait for the pickUpPose action server to start
  navac.waitForServer(); //will wait for infinite time

	ROS_INFO("Waiting for localisation action server to start.");
  // wait for the pickUpPose action server to start
  locac.waitForServer(); //will wait for infinite time

	ros::Subscriber pupsub = n.subscribe("/pickuppose/result", 10, pickUpPoseCallback);		
	ros::Subscriber navsub = n.subscribe("/navigation/result", 10, navigationCallback);
	ros::Subscriber locsub = n.subscribe("/localisation/result", 10, localisationCallback);

	ros::Publisher perception_pub = n.advertise<std_msgs::Int32>("/perception/result", 10);
  ros::Subscriber perceptionsub = n.subscribe("/perception/result", 10, perceptionCallback);

	//ros::Publisher loc_pub = n.advertise<std_msgs::Int32>("/localisation/result", 10);
  //ros::Subscriber locsub = n.subscribe("/localisation/result", 10, localisationCallback);
	
	std_msgs::Int32 defaultValue;
	defaultValue.data = 0;

  ros::Rate loop_rate(10);
  while (ros::ok())
  {
		switch (currentState)
		{
			case IDLE:
				currentState = LOCALISATION;
				break;

			case LOCALISATION:
				if (!locServerBusy)
				{
					ROS_INFO("Lancement de la tache de LOCALISATION");
					locac.sendGoal(locGoal);
					locServerBusy = true;
				}
				break;

			case PERCEPTION:
				if (!perceptionServerBusy)
				{
					ROS_INFO("Lancement de la tache de PERCEPTION");
					perception_pub.publish(defaultValue);
					perceptionServerBusy = true;
				}
				break;

			case MOVING_PICK:
				if (!navServerBusy)
				{
					ROS_INFO("Lancement de la tache de NAVIGATION pour aller SAISIR objet");
					navac.sendGoal(navGoalPick);
					navServerBusy = true;
				}
				break;

			case MOVING_PLACE:
					if (!navServerBusy)
					{
						ROS_INFO("Lancement de la tache de NAVIGATION pour aller DEPOSER objet");
						navac.sendGoal(navGoalPlace);
						navServerBusy = true;
					}
					break;

			case PLACE:
				if (!pupServerBusy)
				{
					ROS_INFO("Lancement de la tache de PICKANDPLACE pour DEPOSER objet");
					pupac.sendGoal(pickPlaceGoal);
					pupServerBusy = true;
				}
				break;

			case PICK:
				if (!pupServerBusy)
				{
					ROS_INFO("Lancement de la tache de PICKANDPLACE pour SAISIR objet");
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
