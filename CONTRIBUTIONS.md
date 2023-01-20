# Liste des contributions par auteurs:

## Martial BAILLY et Théo TRAFNY

- Cartographie des salles 314 et 315 de la MFJA (fichiers .bmp et .yaml)
- Tests de la cartographie à travers des tâches de naviguation décrites par RVIZ
- Correction des scripts ``server_move_to_goal.py`` ``client_move_to_goal.py``
- Control du tapis roulant sur le PMB2 46C:
> Ajout du package ``pmb2_conveyor_control`` et du module utilitaire ``ConveyorController``

Topic: ``/run_conveyor/goal``
Message: ``conveyor_controller_msgs/RunConveyorActionGoal``
```
[conveyor_controller_msgs/RunConveyorActionGoal]:
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
actionlib_msgs/GoalID goal_id
  time stamp
  string id
conveyor_controller_msgs/RunConveyorGoal goal
  std_msgs/Duration duration
    duration data
  uint8 speed
  bool reverse
```

Exemple:

> Voir les exemples fournis dans le README associé au package ``pmb2_conveyor_control``: [Lien](pmb2_conveyor_control/README.md)


## Rémi LABORIE, Fatima EL-HANTATI, Kahina CHALABI

Le travail de ces trois personnes sont sous les commits de reminator329.

### Travail réalisé

Tâche désignée : PMB 42 transporte l'objet de PMB 46 au Tiago 155.

- Création du package sri_transport_object_42 (voir le README de ce package).
- Cartographie des salles 314 et 315 de la MFJA avec le Tiago 42 (sri_transport_object_42/data/mfja_314_315).
- Récupération du fichier launch tiago_navigation_AIP_gazebo.launch et adaptation à notre carte (tiago_navigation_MFJA_gazebo.launch).
- Récupération du script python server_move_rotate.py du package sri_tiago_navigation et adaptation à notre tâche.
- Le multi-Tiago ne fonctionne pas pour l'instant, par conséquent, nous avons créé le point initial et final du robot pour qu'il transporte l'objet entre les deux.

[Lien vers la vidéo démo](https://youtube.com/shorts/DFwC9F1DcuY?feature=share)

### Difficultés rencontrées

Le robot peut être perdu, c'est à dire qu'il ne bouge pas ou ne se dirige pas au bon endroit lors de l'appel du service ```move_rotate_base_42```.</br>
Il faut penser à vérifier l'estimation de sa pose sur RViz. Il faudrait que le robot se rende compte qu'il est perdu, en analysant par exemple l'erreur d'estimation de la pose du robot : la covariance. </br>
</br>
On a dû ajouter un support pour récupérer l'object donnée par Tiago 46 car ce dernier voit le robot 42 comme un obstacle. Pour cette raison, le robot 46 s'arrête à une certaine distance du 42 ce qui empêche l'objet de tomber sur la base du robot.


## Zineddine OUALI & Alexandre LOTTE (resp @ZineddineOuali et @AlexLtte)

- Correction de l'estimation de la position de l'objet
- Filtrage des configurations par contraintes sur la sphère des configurations accessibles par le bras du robot et affichage des configurations filtrées sur RVIZ
- Réglage des offsets selon les objets manipulés
- Modification de l'objet pour une meilleure prise (Canette Lipton© Pastèque-Menthe auto-financée (investissement))
Milestone : La tâche de pick est opérationnelle sur Tiago.
```
