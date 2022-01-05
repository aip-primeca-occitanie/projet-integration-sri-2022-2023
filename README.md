# projet-integration-sri-2021-2022
Projet d'intégration ROS SRI 2021 2022

# Organization:

[Planification de tâches]()

[Perception]()

[Simulation](aip_gazebo) 

[Navigation](navigation/README.md):


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
- Dans un terminal dans la racine du projet, lancer :
```bash
source ./devel/setup.bash
roslaunch aip_gazebo shuttle_only.launch
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

