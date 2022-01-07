Le package sri_tiago_pick permet de lancer une opération de saisie dans la simulation du monde. Celle-ci est basée sur le tutoriel de pick de tiago mais légèrement modifié pour qu'il soit adapté au monde groix_porquerolles.world. 

Une démo peut être lancée en utilisant trois terminaux différents (voir démo ci dessous). Celle-ci fait apparaître le robot devant une table du monde et lance une opération de pick. Le robot doit d'abord détecter le cube via son QR-Code puis déplace son bras avec une opération de saisie que le robot choisi. La position en x est légèrement modifiée dans le code afin de calibrer la position de saisie par rapport à la réelle position du cube. Sans cette calibration, le bras du robot était mal placé et poussait le cube. Lorsque le robot a bien saisi le cube, il le soulève et la démo se termine. Précédemment, le robot posait juste après le cube au même endroit qu'il se trouvait, mais ce place a été enlevé pour tenter d'en effectuer un en lisant un QR Code. Ce service ros /place_gui est également disponible dans ce package pour tenter de reconnatre le QR code du même cube sur la table pour simuler un place, mais le robot n'arrive pas à planifier sa trajectoire dans le monde.

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

- Dans un 3eme terminal dans la racine du projet, lancer le service pick :
```bash
source ./devel/setup.bash
rosservice call /pick_gui
```
