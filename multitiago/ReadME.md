#### Dépendances : 

 tiago_gazebo
 tiago_multi
 aip_gazebo
 gazebo_ros 
 pal_gazebo_worlds



### INITIALISATION
- On va dans le ws et on le source 
```bash
cd workspace  
source ./devel/setup.bash  
```
- Lancement de la simulation simple  
```bash
roslaunch tiago_multi multitiago_gazebo.launch  
```

### CHANGER LA PINCE EN SIMULATION 
- Aller dans le launch_tiago.launch   
```bash
roscd tiago_multi  
cd launch/  
nano launch_tiago.launch  
```
- et changer le default "hey5" pour la main "gripper" pour la pince   
### BOUGER LES ROBOTS SEPAREMMENT
```bash
rosrun play_motion run_motion offer_gripper /play_motion:=/tiago1/play_motion  
rosrun play_motion run_motion wave /play_motion:=/tiago2/play_motion  
```
- Liste des options dans mvmts_predefs.txt ci-joint  



### NAVIGATION
- Lancement de la simulation avec map pour navigation rviz  
```bash
roslaunch tiago_multi multitiago_gazebo_navigation.launch  
```

### CHANGER LA MAP  
- Changer dans le dossier tiago_multi/launch le lien vers le dossier des maps et le world  
```bash
roscd tiago_multi  
cd launch  
nano multitiago_gazebo_navigation.launch   
```
#<arg name="map" default="VOTRE_CHEMIN_VERS_DOSSIER"  
#<include file=$ ... "LE_CHEMIN_VERS_AIP_GAZEBO"  

