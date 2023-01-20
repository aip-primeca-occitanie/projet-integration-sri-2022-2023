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