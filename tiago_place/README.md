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
1. /aruco_single
2. /pick_and_place_server
3. /pick_client
4. /rviz
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

