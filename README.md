# projet-integration-sri-2021-2022
Projet d'intégration ROS SRI 2021 2022

# Organization:

[Planification de tâches]()

[Perception]()

[Simulation](aip_gazebo) 

[Navigation](navigation/README.md): Hakim Cherfi & Jeremy Santene

[Multitiago](multitiago/README.md): Rémi Delauzun & Raphaël Bizet

Plannification de mouvement

# Demos

## Simulations

### Monde simple
Lancer une simulation simple dans groix_porquerolles.world : 
- Dans un terminal dans la racine du projet, lancer :

```bash
source ./devel/setup.bash
roslaunch aip_gazebo aip_gazebo.launch
```

### Simulation cellule + navette
Lancer une simulation de la cellule flexible de la salle groix_porquerolles avec une navette montée sur les rails.
- Pour lancer la simulation, dans un terminal dans la racine du projet, lancer :
```bash
source ./devel/setup.bash
roslaunch aip_gazebo shuttle_only.launch
```
- Pour visualiser les topics crées par la simulation, lancer :
```bash
rostopic list
```
resultat attendu :
```bash
...
/my_shuttle/joint1_vel_controller/command
/my_shuttle/joint2_vel_controller/command
/my_shuttle2/joint1_vel_controller/command
/my_shuttle2/joint2_vel_controller/command
...
```

- Pour controller les navettes de cette simulation entrez la commande suivante :
```bash
#Pour controller la navette 1 à une vitesse de 3.0 :
rostopic pub /my_shuttle/joint1_vel_controller/command std_msgs/Float64 "data: -3.0"
#Pour controller la navette 2 à une vitesse de 3.0 :
rostopic pub /my_shuttle2/joint1_vel_controller/command std_msgs/Float64 "data: -3.0"
```



	
### Saisie
Lancer une opération de saisie dans la simulation :
- Dans un 2eme terminal dans la racine du projet, lancer les noeuds ROS :
```bash
source ./devel/setup.bash
roslaunch sri_tiago_pick pick_demo.launch
```

- Dans un 3eme terminal dans la racine du projet, lancer le servilc pick and place:
```bash
source ./devel/setup.bash
rosservice call /pick_gui
```

### Navigation

À la racine du projet, sourcer ```devel/setup.bash``` et lancer la commande

``` code
roslaunch navigation aip_tiago_mapping.launch
```

Ceci permet de créer une carte de la salle porquerolles en faisant naviguer le robot (simulation).


### Multitiago

Dans un terminal dans la racine du projet, lancer :

```bash
source ./devel/setup.bash
roslaunch multitiago multi_aip_gazebo.launch
```
Lancement d'une simulation de deux robots tiago dans la salle groix-porquerolle.
![image d'illustration](https://github.com/aip-primeca-occitanie/projet-integration-sri-2021-2022/blob/main/multitiago/screenshots/multitiago_simulation.png?raw=true)

