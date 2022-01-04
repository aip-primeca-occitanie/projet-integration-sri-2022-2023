# Comment lancer la simulation de Pick & Place du projet
Avec les fichiers présents dans le dossier *motion_planning*. Ce dossier contient le code nécessaire pour permettre au robot d'attraper un objet défini avec sa pince (*pick*) puis de le poser (*place*).

**Assurez-vous d'avoir correctement initialisé et sourcé l'environnement de travail avant de commencer.**

### Initialisation du terminal
La construction de l'environnement de travail ROS doit avoir été faite au préalable.
Lancez un terminal dans le répertoire racine de *votre* environnement de travail, puis exécutez la commande `source ./devel/setup.bash`.

### Lancement de Gazebo et RVIZ
Lancez la simulation Gazebo du pick and place :
`roslaunch motion_planning pick_simulation.launch`
Au moment du lancement, le bras du robot dans Gazebo va se mettre à bouger pour se placer dans sa configuration initiale.

Puis lancez la visualisation RVIZ de cette simulation :
`roslaunch motion_planning pick_demo.launch`

Vous devriez appercevoir dans les deux logiciels le robot Tiago modélisé, avec devant lui une table et l'objet à saisir posé dessus.

### Lancement des tâches de Pick & Place
Lancez la tâche d'attrapage de l'objet avec la commande suivante :
`rosservice call /pick_gui`
Dans Gazebo et RVIZ, vous devriez voir le bras du robot se mettre en mouvement, puis tenter d'attraper l'objet posé devant lui. Il n'est pas impossible qu'il échoue ou fasse tomber l'objet.

Lorsque l'objet est attrapé, vous pouvez lancer la tâche pour le poser avec la commande suivante :
`rosservice call /place_gui`
