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

Tâche désignée : PMB 42 transporte l'objet de PMB 46 au Tiago 155.

- Création du package sri_transport_object_42.
- Cartographie des salles 314 et 315 de la MFJA avec le Tiago 42 (sri_transport_object_42/data/mfja_314_315).
- Récupération du fichier launch tiago_navigation_AIP_gazebo.launch et adaptation à notre carte (tiago_navigation_MFJA_gazebo.launch).
- Récupération du script python server_move_rotate.py du package sri_tiago_navigation et adaptation à notre tâche.
- Le multi-Tiago ne fonctionne pas pour l'instant, par conséquent, nous avons créé le point initial et final du robot pour qu'il transporte l'objet entre les deux.
