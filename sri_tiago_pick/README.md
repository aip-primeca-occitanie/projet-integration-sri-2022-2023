Le package sri_tiago_pick permet de lancer une opération de saisie et de pose sur le robot. Celle-ci est basée sur le tutoriel de pick de tiago mais  modifié pour qu'il puisse attraper correctement la canette (nouvel objet introduit cf vidéo d'illustration de la manipulation). 

Une démo peut être lancée en utilisant trois terminaux différents (voir démo ci dessous). Celle-ci fait apparaître le robot devant une table du monde et lance une opération de pick. Le robot doit d'abord détecter le cube via son marqueur Aruco puis déplace son bras avec une opération de saisie que le robot choisi. La position en x est légèrement modifiée dans le code afin de calibrer la position de saisie par rapport à la réelle position du cube. Sans cette calibration, le bras du robot était mal placé et poussait le cube. Lorsque le robot a bien saisi le cube, il le soulève et la démo se termine. Précédemment, le robot posait juste après le cube au même endroit qu'il se trouvait, mais ce place a été enlevé pour tenter d'en effectuer un en lisant un Aruco. Ce service ros /place_gui est également disponible dans ce package pour tenter de reconnaître le marqueur Aruco du même cube sur la table pour simuler un place, mais le robot n'arrive pas à planifier sa trajectoire dans le monde.

### Mise en place 
Pour compiler le projet, vous pouvez utiliser la commande suivante à la racine du projet :
```
catkin_make_isolated
```
Puis sourcer le terminal avec :
```
source devel_isolated/setup.bash
```
OU

Pour compiler seulement ce package, vous pouvez utiliser la commande suivante :
```
catkin_make_isolated --pkg sri_tiago_pick
```
Et sourcer avec :
```
source devel_isolated/sri_tiago_pick/setup.bash
```

### Pick
Lancer une opération de Pick sur le robot :
- Dans un terminal sourcé, lancer les noeuds ROS :
```
roslaunch sri_tiago_pick pick_demo.launch
```

- Dans un second terminal sourcé, lancer le service pick :
```
rosservice call /pick_gui
```

### Place
Lancer une opération de Place dans la simulation :
- Dans un premier terminal sourcé, lancer les noeuds ROS :
```
roslaunch sri_tiago_pick place_demo.launch
```

- Dans un second terminal sourcé, lancer le service place :
```
rosservice call /place_gui
```

### Note importante

Bien faire attention aux offsets rajoutés dans le code "pick_client.py", ils ont été ajustés spécifiquement pour nos conditions d'expérience, donc pour conditions différentes, les ajuster.
