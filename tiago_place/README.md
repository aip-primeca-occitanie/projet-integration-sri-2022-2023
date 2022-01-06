# Package tiago_pick
Package dedié au placement d'un objet sur une table & l'aide d'un QR code


__Alexandre Baures & Clément Petit__

## Simulations
Pour lancer la simulation:

Lancement de la simulation dans Gazebo :
- Dans un 1eme terminal dans la racine du projet :
```bash
source ./devel/setup.bash
roslaunch tiago_pick_demo pick_simulation.launch
```
Lancement des noeuds :
/aruco_single: ArUco marker detector node

/pick_and_place_server: node in charge of defining the planning scene, request pick and plans with MoveIt! and execute them.

/pick_client: node that prepares the robot for the object detection and the pick and place operations: raises the arm to a safe pose and lowers the head to look at the table. Then it waits until the object marker is detected and its pose is retrieved in order to send a goal to the /pick_and_place_server.

/rviz: in order to visualize all the steps involved in the demo.

- Dans un 2eme terminal dans la racine du projet:
```bash
source ./devel/setup.bash
roslaunch tiago_pick_demo pick_demo.launch
```

Lancement de la démo:
- Dans un 3eme terminal dans la racine du projet:
```bash
source ./devel/setup.bash
rosservice call /pick_gui
```

