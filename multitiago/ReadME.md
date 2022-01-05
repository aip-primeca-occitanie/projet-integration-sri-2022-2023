#### Dépendances : 

 tiago_gazebo
 tiago_multi
 aip_gazebo
 gazebo_ros 
 pal_gazebo_worlds



### INITIALISATION
#on va dans le ws et on le source
cd workspace
source ./devel/setup.bash

#lancement de la simulation simple
roslaunch tiago_multi multitiago_gazebo.launch

### CHANGER LA PINCE EN SIMULATION 
#aller dans le launch_tiago.launch 
roscd tiago_multi
cd launch/
nano launch_tiago.launch
#et changer le default "hey5" pour la main "gripper" pour la pince 

#bouger les robots séparemment
rosrun play_motion run_motion offer_gripper /play_motion:=/tiago1/play_motion
rosrun play_motion run_motion wave /play_motion:=/tiago2/play_motion

#Liste des options dans mvmts_predefs.txt ci-joint



### NAVIGATION
#lancement de la simulation avec map pour navigation rviz
roslaunch tiago_multi multitiago_gazebo_navigation.launch

### CHANGER LA MAP  
#changer dans le dossier tiago_multi/launch le lien vers le dossier des maps et le world
roscd tiago_multi
cd launch
nano multitiago_gazebo_navigation.launch 
#<arg name="map" default="VOTRE_CHEMIN_VERS_DOSSIER"
#<




#dans ce dossier appeller la map mmap.yaml car le .py qui cherche dans le dossier cherche en hard un mmap.yaml
 roscd pal_navigation_sm
cd scripts
nano map_setups.py
