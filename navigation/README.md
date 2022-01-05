# README Navigation

launch mapping simulation:

Commande pour lancer le mapping dans la salle groix

```code
roslaunch navigation aip_tiago_mapping
```

topic ROS pour ordre de navigation : move_base_simple/goal

``` bash
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
geometry_msgs/Pose pose
  geometry_msgs/Point position
    float64 x
    float64 y
    float64 z
  geometry_msgs/Quaternion orientation
    float64 x
    float64 y
    float64 z
    float64 w
```
