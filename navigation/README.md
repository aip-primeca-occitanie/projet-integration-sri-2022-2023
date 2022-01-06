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

Pour appeler le service et donc transmettre au topic demandant au robot de se déplacer à un point demandé :

``` bash
rosservice call /move_base "seq: 0
stamp: {secs: 0, nsecs: 0}
frame_id: ''
x: 0.0
y: 0.0
z: 0.0
xr: 0.0
yr: 0.0
zr: 0.0
wr: 1.0"
```

Testé en simulation.
