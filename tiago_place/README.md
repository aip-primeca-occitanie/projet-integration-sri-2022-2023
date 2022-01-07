## Package tiago_pick
__Alexandre Baures & Clément Petit__

Package dedié au placement d'un objet sur une table & l'aide d'un QR code.
Ce package n'est pas encore fonctionnelle, il subsiste des erreurs.

Voir la partie qui fonctionne
[motion_planning]()

Les deux scripts principaux sont:
- pick_and_place_server.py
- pick_client.py


## Simulations
Pour lancer la simulation:

Lancement de la simulation dans Gazebo :
- Dans un 1eme terminal dans la racine du projet :
```bash
source ./devel/setup.bash
roslaunch tiago_pick_demo pick_simulation.launch
```
Lancement des noeuds :
 */aruco_single*
 */pick_and_place_server*
 */pick_client*
 */rviz*
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

