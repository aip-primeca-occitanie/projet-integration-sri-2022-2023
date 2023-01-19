# README SRI_TIAGO_NAVIGATION

## Première étape : launch mapping simulation

Commande pour lancer le mapping dans la salle groix de l'aip

```code
roslaunch sri_tiago_navigation aip_tiago_mapping.launch
```

(Ce fichier a été construit à partir des fichiers launch déjà fournis exploitant la map de l'aip, en y ajoutant l'appel à rviz ainsi qu'à navigation et definitions de variables (mapping notamment))

Commande pour lancer le mapping dans les salles 314 - 315 de la MFJA en simulation.

```code
roslaunch sri_tiago_navigation tiago_navigation_MFJA_gazebo.launch
```

Commande pour faire bouger le robot sur RViz.

```code
rosrun key_teleop key_teleop.py
```

## Deuxième étape : création d'un service pour publier sur le topic /move_base_simple/goal

Compiler le paquet, sans oublier de sourcer dans chaque terminal depuis le répertoire de travail ```./devel/setup.bash``` 

Se SSH au robot, récuperation de la carte : ```rosservice call /pal_map_manager/change_map "input: 'salle_314_mfja'"```

(Les cartes se trouvent dans ```$HOME/.pal/maps/configurations```.)

(Lancement du service : ```rosrun navigation server_move.py```)
Lancement du service : ```rosrun sri_tiago_navigation server_move_rotate.py```

(Appel au service : ```rosservice call /sri23/move_base  "x: 0.0
y: 0.0
theta: 0.0"```)
Appel au service : ```rosservice call /sri23/move_rotate_base  "x: 0.0
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

(```theta``` n'a pas d'influence sur l'orientation demandée, le quaternion transmis vaut (0,0,0,1), ```z``` vaut ```0```. ```seq```, ```stamp``` sont gérés automatiquement, ```frame_id``` vaut ```"map"```.)
```theta``` est pris en compte dans l'orientation demandée dans le repère de la map.

[Lien démo](https://www.youtube.com/watch?v=SU8ofjLCdqI)

## PMB2 Navigation repère monde

Après avoir source le package ``sri_tiago_navigation``:

Vous pouvez lancer RVIZ et le serveur de naviguation via la commande suivante:
```bash
roslaunch sri_tiago_navigation pmb2_navigation_MFJA.launch
```

Et lancer une commande de naviguation par le client:
```bash
rosrun sri_tiago_navigation client_move_to_goal.py <location_name>
```

(locations: ``milieu``, ``milieu-test``)