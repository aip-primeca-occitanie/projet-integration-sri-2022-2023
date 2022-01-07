#### Dépendances : 

 tiago_gazebo
 tiago_multi
 aip_gazebo
 gazebo_ros 
 pal_gazebo_worlds

- Pour être sur, installer tiago_public_ws avec les tutoriels tiago ros pour melodic. 
http://wiki.ros.org/Robots/TIAGo/Tutorials/Installation/InstallUbuntuAndROS
- Exécuter à partir du 2. si déjà sur Ubuntu 18 

- Si sur Ubuntu 20, remplacer tous les melodic par noetic lors du tutoriel

### INITIALISATION
- On va dans le ws et on le source 
```bash
cd _VOTRE_WORKSPACE  
source ./devel/setup.bash  
```
- Lancement de la simulation simple pour vérifier la présence des packages annexes
```bash
roslaunch tiago_multi multitiago_gazebo.launch  
```

### BOUGER LES ROBOTS SEPAREMMENT
```bash
rosrun play_motion run_motion offer_gripper /play_motion:=/tiago1/play_motion  
rosrun play_motion run_motion wave /play_motion:=/tiago2/play_motion  
```
- Liste des options dans mvmts_predefs.txt ci-joint  


### CHANGER LA PINCE EN SIMULATION 
- Aller dans le launch_tiago.launch   
```bash
roscd tiago_multi  
cd launch/  
nano launch_tiago.launch  
```
- et changer le default "hey5" pour la main "gripper" pour la pince   

### CHANGER LA MAP  
- Tout est implémenté dans le dossier map_rr 
```bash
cd aip_multitiago/config/map_rr
```
- et changer les .yaml avec les votres. 

Pour référencer un nouveau dossier différent, le créer dans le config précédent, puis changer la ligne suivant dans le launch appelé précedemment
```bash
nano ./launch/multi_aip_gazebo.launch  
#<arg name="map" default="$(find aip_multitiago)/config/VOTRE_DOSSIER "
```



### NAVIGATION
- Lancement de la simulation dans la carte de l'aip pour navigation rviz  
```bash
roslaunch aip_multitiago multi_aip_gazebo.launch  
```

- Parfois on obtient un lien manquant entre l'odom et la map, ce qui est accompagné de messages d'erreurs "couldn't match fooprint & map", et qu'on peut visualiser avec la commande 
```bash 
rosrun rqt_tf_tree rqt_tf_tree 
```
dont voici le résultat attendu lorsque tout fonctionne : 
![image d'illustration](https://github.com/aip-primeca-occitanie/projet-integration-sri-2021-2022/blob/main/multitiago/screenshots/tree.png?raw=true)


