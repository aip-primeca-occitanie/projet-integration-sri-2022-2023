## Package tiago_pick
__Alexandre Baures & Clément Petit__

Package dedié au placement d'un objet sur une table & l'aide d'un QR code.
Ce package n'est pas encore fonctionnelle, il subsiste des erreurs.

Voir la partie qui fonctionne [ici](https://github.com/aip-primeca-occitanie/projet-integration-sri-2021-2022/tree/main/motion_planning)

- pick_and_place_server.py :
  - fait des appels aux pick_client afin de récupérer les positions des QR code. Lance les mouvements du robot pour pick et place aux positions désirées. 
- pick_client.py :
  - initialise le robot à des positions données. Et appelle Aruco pour détecter les QR code et calculer leur position.


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

