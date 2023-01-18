# Liste des contributions par auteurs:

## Martial BAILLY et Théo TRAFNY

- Cartographie des salles 314 et 315 de la MFJA (fichiers .bmp et .yaml)
- Tests de la cartographie à travers des tâches de naviguation décrites par RVIZ
- Control du tapis roulant sur le PMB2 46C:

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

Faire tourner le tapis roulant pendant 3 secondes à une certaines vitesse
```bash
rostopic pub -1 /run_conveyor/goal conveyor_controller_msgs/RunConveyorActionGoal "{header: {seq: 0, stamp: {secs: 0, nsecs: 0}, frame_id: ''}, goal_id: {stamp: {secs: 0, nsecs: 0}, id: ''}, goal: {duration: {data: {secs: 3, nsecs: 0}}, speed: 1}}"
```