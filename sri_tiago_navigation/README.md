# README SRI_TIAGO_NAVIGATION

## Première étape : launch mapping simulation

Commande pour lancer le mapping dans la salle groix de l'aip

```code
roslaunch sri_tiago_navigation aip_tiago_mapping.launch
```

(Ce fichier a été construit à partir des fichiers launch déjà fournis exploitant la map de l'aip, en y ajoutant l'appel à rviz ainsi qu'à navigation et definitions de variables (mapping notamment))

## Deuxième étape : création d'un service pour publier sur le topic /move_base_simple/goal

Compiler le paquet, sans oublier de sourcer dans chaque terminal depuis le répertoire de travail ```./devel/setup.bash``` 

Se SSH au robot, récuperation de la carte : ```rosservice call /pal_map_manager/change_map "input: 'salle_groix'"```

(Les cartes se trouvent dans ```$HOME/.pal/maps/configurations```.)

Lancement du service : ```rosrun navigation server_move.py```

Appel au service : ```rosservice call /sri22/move_base  "x: 0.0
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

```theta``` n'a pas d'influence sur l'orientation demandée, le quaternion transmis vaut (0,0,0,1), ```z``` vaut ```0```. ```seq```, ```stamp``` sont gérés automatiquement, ```frame_id``` vaut ```"map"```.

[Lien démo](https://www.youtube.com/watch?v=SU8ofjLCdqI)
