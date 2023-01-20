# README SRI_TIAGO_NAVIGATION

## Première étape : launch mapping simulation

Commande pour lancer le mapping dans les salles 314 - 315 de la MFJA en simulation.

```code
roslaunch sri_tiago_navigation tiago_navigation_MFJA_gazebo.launch
```

Commande pour faire bouger le robot sur RViz.

```code
rosrun key_teleop key_teleop.py
```

## Deuxième étape : création d'un service pour publier sur le topic /move_base_simple/goal, pour faire bouger le robot à une pose précise (X,Y, theta) selon le repère de la carte 

Compiler le paquet (catkin_make_isolated --pkg sri_transport_object_42), sans oublier de sourcer dans chaque terminal depuis le répertoire de travail ```./devel_isolated/sri_transport_object_42/setup.bash```

Se SSH au robot, récuperation de la carte : ```rosservice call /pal_map_manager/change_map "input: 'mfja_312_314'"```
(la carte a été upload sur le robot auparavant, les cartes se trouvent dans ```$HOME/.pal/maps/configurations```.)

Lancement du service : ```rosrun sri_transport_object_42 server_move_rotate_42.py```


Appel au service en spécifiant la pose : ```rosservice call /sri23/move_rotate_base_42  "x: 0.0
y: 0.0
theta: 0.0"```

Ce service publie sur le topic ROS pour ordre de navigation : ```move_base_simple/goal```

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


## Position du robot 42

Init : x = 2.0 ; y = -1.0 ; theta = -2.5
End : x = -6 ; y = -6 ; theta = -2.5
