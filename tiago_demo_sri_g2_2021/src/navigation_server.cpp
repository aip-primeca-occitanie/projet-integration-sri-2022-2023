#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <tiago_demo_sri_g2_2021/NavigationAction.h>

class NavigationAction
{
protected:

  ros::NodeHandle nh_;
  actionlib::SimpleActionServer<tiago_demo_sri_g2_2021::NavigationAction> as_; // NodeHandle instance must be created before this line. Otherwise strange error occurs.
  std::string action_name_;
  // create messages that are used to published feedback/result
  tiago_demo_sri_g2_2021::NavigationFeedback feedback_;
  tiago_demo_sri_g2_2021::NavigationResult result_;

public:

  NavigationAction(std::string name) :
    as_(nh_, name, boost::bind(&NavigationAction::executeCB, this, _1), false),
    action_name_(name)
  {
    as_.start();
  }

  ~NavigationAction(void)
  {
  }

  void executeCB(const tiago_demo_sri_g2_2021::NavigationGoalConstPtr &goal)
  {
    // helper variables
    ros::Rate r(1);
    bool success = true;

    // publish info to the console for the user
    ROS_INFO("%s: Executing, navigation sequence to reach x = %f y = %f ", action_name_.c_str(), goal->target.pose.position.x, goal->target.pose.position.y);

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
  ros::init(argc, argv, "navigation_server");

  NavigationAction navigation("navigation");
  ros::spin();

  return 0;
}
