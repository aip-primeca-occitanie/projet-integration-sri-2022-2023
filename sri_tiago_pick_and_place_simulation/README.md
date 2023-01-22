## Package sri_tiago_place
__Pailler Vincent & Dorian Bordes__

Package dedié a la récupération d'un objet sur une table & l'aide d'un QR code puis au replacement de cet objet au même endroit via simulation.
Ce package n'est pas encore fonctionnelle, il subsiste des erreurs. En effet la simulation n'est pas encore 100% fiable.

Fichier utilisé :
- pick_and_place_server.py :
  - fait des appels aux pick_client afin de récupérer les positions des QR code. Lance les mouvements du robot pour pick et place aux positions désirées. 
- pick_client.py :
  - initialise le robot à des positions données. Et appelle Aruco pour détecter les QR code et calculer leur position.

## Simulations
Pour lancer cette partie il faut préalablement effectuer quelques opérations pour acceder aux packets.
Executer la commande suivante à la racine du projet.
```bash
catkin_make_isolated
source devel_isolated/setup.bash
```
Ensuite il faut lancer la simulation. L'environnement utilisé est celui de l'ancien AIP. L'environnement monde de la MFJA peut aussi être utilisé.
 Dans un 1eme terminal dans la racine du projet :
```bash
roslaunch aip_gazebo aip_gazebo.launch
```

Lancement de la simulation dans rviz :
- Dans un 2eme terminal dans la racine du projet :
Lancement des noeuds :
 */aruco_single*
 */pick_and_place_server*
 */pick_client*
 */rviz*
```bash
source devel_isolated/setup.bash
roslaunch sri_tiago_place place_demo.launch
```

Lancement de la démo:
- Dans un 3eme terminal dans la racine du projet:
```bash
source ./devel_isolated/setup.bash
rosservice call /pick_and_place_gui
```
