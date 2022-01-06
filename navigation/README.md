# README Navigation

## Première étape : launch mapping simulation

Commande pour lancer le mapping dans la salle groix de l'aip

```code
roslaunch navigation aip_tiago_mapping.launch
```

(Ce fichier a été construit à partir des fichiers launch déjà fournis exploitant la map de l'aip, en y ajoutant l'appel à rviz ainsi qu'à navigation et definitions de variables (mapping notamment))

## Deuxième étape : création d'un service pour publier sur le topic /move_base_simple/goal

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
