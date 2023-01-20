# README SRI_TIAGO_NAVIGATION
# *Paquet pour la nvigation du robot reel et simulation sur Gazebo*

Avant tout :
Compiler le paquet, sans oublier de sourcer dans chaque terminal depuis le repertoire de travail ```./devel/setup.bash```

## Mise a jour des cartes
- La collecte du nuage de points de la carte se fait par la navigation manuelle du Tiago (ou Pal Mobile Base) autour de la piece. Elle doit etre sauvegardee et mise a jour au niveau du robot.

Se SSH au robot, recuperation de la carte : ```rosservice call /pal_map_manager/change_map "input: 'mfja_314_315'"```

```code
export ROS_MASTER_URI=http://<robot>:11311
export ROS_IP=<ifconfig : IP ordinateur>
```

(Les cartes se trouvent dans ```$HOME/.pal/maps/configurations```.)

## Simulation de la navigation sur Gazebo
Apres avoir source le package sri_tiago_navigation :

Afin de lancer la simulation Gazebo (PAS SUR LE ROBOT) avec la carte desiree, lancer la commande :

```code
roslaunch sri_tiago_navigation tiago_navigation_gazebo.launch world:=mfja_314_315
```

Le dossier 'mfja_314_315' dans le dossier data du package contient la carte des salles 314 et 315 de la MFJA. Pour changer de carte, il suffit d'assigner a world le nom d'un autre dossier de carte (a mettre dans le dossier data).

## Visualisation et navigation du robot depuis RViz
Afin de lancer Rviz (sur l'ordinateur local, ou sur le robot), lancer la commande :

```code
roslaunch sri_tiago_navigation tiago_navigation.launch world:=mfja_314_315
```

# Plannification de la trajectoire du robot reel (ou simule) depuis RViz
D'abord lancer un node (RViz doit d'abord etre lance avec la commande precedente)

```code
rosrun sri_tiago_navigation positions_planner.py
```

Puis pointer sur RViz les points d'interets de la trajectoire a partir de l'outil 'Publish Point'
Ensuite lancer dans un nouveau terminal (toujours source pour la package sri_tiago_navigation) le service pour que le robot effectue la trajectoire :

```code
rosservice call /sri23/trajectory_planner "{}"
```
## Services de navigation
Il y a deux services de navigation :
- Pour definir une position a atteindre (sans considerer l'orientation) :

```code
rosrun sri_tiago_navigation server_move.py
```

Apres, lancer le service associe

```code
rosservice call /sri23/move_base "x: 0.0 y: 0.0 theta: 0.0"
```

```theta``` n'est pas pris en compte dans l'orientation demandee dans le repere de la map.

- Pour definir une pose a atteindre (Prise en compte de la position et de l'orientation) :

```code
rosrun sri_tiago_navigation server_move_rotate.py
```

Apres, lancer le service associe

```code
rosservice call /sri23/move_rotate_base "x: 0.0 y: 0.0 theta: 0.0"
```

```theta``` est pris en compte dans l'orientation demandee dans le repere de la map.

Ces services publient sur le topic ROS : ```move_base_simple/goal```

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

## Tuto / Demo
[Lien demo 2021-2022](https://www.youtube.com/watch?v=SU8ofjLCdqI)

- Service pour positionner le robot sur la map
[Demo positionnement du robot (YouTube)]()
- Service pour positionner le robot sur la map avec une orientation desiree
[Demo positionnement et orientation du robot (YouTube)]()
- Service pour plannifier la trajectoire du robot par des points successifs sur RViz
[Demo plannification de trajectoire du robot (YouTube)]()

## PMB2 Navigation repere monde

Apres avoir source le package ``sri_tiago_navigation``:

Vous pouvez lancer RVIZ et le serveur de naviguation via la commande suivante:
```bash
roslaunch sri_tiago_navigation pmb2_navigation_MFJA.launch
```

Et lancer une commande de naviguation par le client:
```bash
rosrun sri_tiago_navigation client_move_to_goal.py <location_name>
```

(locations: ``milieu``, ``milieu-test``)
