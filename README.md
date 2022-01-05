# projet-integration-sri-2021-2022
Projet d'intégration ROS SRI 2021 2022

# Organization:

Planification de tâches: 
	

Perception: 

Simulation: 


Navigation:


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

