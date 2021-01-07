#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <tiago_demo_sri_g2_2021/PickUpPoseAction.h>

class PickUpPoseAction
{
protected:

  ros::NodeHandle nh_;
  actionlib::SimpleActionServer<tiago_demo_sri_g2_2021::PickUpPoseAction> as_; // NodeHandle instance must be created before this line. Otherwise strange error occurs.
  std::string action_name_;
  // create messages that are used to published feedback/result
  tiago_demo_sri_g2_2021::PickUpPoseFeedback feedback_;
  tiago_demo_sri_g2_2021::PickUpPoseResult result_;

public:

  PickUpPoseAction(std::string name) :
    as_(nh_, name, boost::bind(&PickUpPoseAction::executeCB, this, _1), false),
    action_name_(name)
  {
    as_.start();
  }

  ~PickUpPoseAction(void)
  {
  }

  void executeCB(const tiago_demo_sri_g2_2021::PickUpPoseGoalConstPtr &goal)
  {
    // helper variables
    ros::Rate r(1);
    bool success = true;


    // publish info to the console for the user
    ROS_INFO("%s: Executing, PickUpPose sequence to grab item detected in frame : %s at location x = %f y = %f z = %f ", action_name_.c_str(), goal->item_target.header.frame_id.c_str(), goal->item_target.point.x, goal->item_target.point.y, goal->item_target.point.z);

    // start executing the action
    for(int i=1; i<=10; i++)
    {
      ROS_INFO("%s: sequence numero %i", action_name_.c_str(), i);
      // check that preempt has not been requested by the client
      if (as_.isPreemptRequested() || !ros::ok())
      {
        ROS_INFO("%s: Preempted", action_name_.c_str());
        // set the action state to preempted
		result_.result_code = 1;
        as_.setPreempted(result_);
        success = false;
        break;
      }
      // this sleep is not necessary, the sequence is computed at 1 Hz for demonstration purposes
      r.sleep();
    }

    if(success)
    {
      ROS_INFO("%s: Succeeded", action_name_.c_str());
      // set the action state to succeeded
	  result_.result_code = 0;
      as_.setSucceeded(result_);
	
    }
  }


};


int main(int argc, char** argv)
{
  ros::init(argc, argv, "pickuppose_server");

  PickUpPoseAction pickuppose("pickuppose");
  ros::spin();

  return 0;
}
