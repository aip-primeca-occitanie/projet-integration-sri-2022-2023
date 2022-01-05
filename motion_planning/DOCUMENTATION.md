# Documentation de la partie *motion_planning*

## Fichiers *.launch*
 `pick_simulation.launch` : permet de créer le robot et son environnement dans Gazebo, avec un appel au fichier *.launch* dédié fourni par Tiago (fichier `tiago_gazebo.launch` présent quelque part dans le dossier *tiago_public_ws*). Dans les paramètres utilisés on a notamment le type du robot (ici, *steel*, donc avec une pince) et son environnement (ici *tabletop_cube*, environnement prédéfini disponible dans *tiago_public_ws/src/tiago_simulation/tiago_gazebo/worlds/* et qui utilise des éléments qui se trouvent dans *tiago_public_ws/src/tiago_simulation/tiago_gazebo/models/*). **Fichier récupéré du tutoriel *pick* de Tiago-Gazebo**     
 
 `pick_demo.launch` : ce fichier a deux rôles : créer le visionnage RVIZ et lier les fichiers pour le Pick & Place à la simulation Gazebo.   
 Les fichiers importants appelés sont *config/pick_motions.yaml* et ceux permettant de créer le node *pick_and_place_serveur*, *pick_and_place_server.py* et *config/pick_and_place_params.yaml*.   
 Enfin, deux nodes sont créés pour les manipulations : *pick_client* et *place_client*, appelant *pick_client.py* et *place_client.py*; ainsi que leurs modélisations sur RVIZ gérées par *config/rviz/tiago_pick_demo.rviz*.   
 **Restent à faire : *pick_client.py*, *config/rviz/tiago_place_demo.rviz* et potentiellement *config/place_motions.yaml*** (en gros tout ce qui permet de créer et exécuter le node *place_client*).   
 **Fichier récupéré du tutoriel *pick* de Tiago-Gazebo**

`pick_sri.launch` : similaire à *pick_demo.launch* mais ne gère pas l'affichage RVIZ et lance deux nodes supplémentaires : *motion_planning_server* et *node_prise* basés sur les fichiers *motion_planning_server.py* et *node_prise.py*.   
**Fichier créé par les étudiants SRI de 2020-2021**

## Fichiers de scripts

`pick_and_place_server.py` : gère la partie serveur du pick & place.   
Permet de créer les services de pick et de place, avec la partie "place" à priori complète.

`pick_client` : permet de gérer la tâche d'attrapage de l'objet.   
- Crée les services */place_gui* et */pick_gui* avec la classe *SphericalService*. **--> Pourquoi */place_gui*  est-il créé ici ?**
- La classe *PickAruco* gérant l'attrapage existe, **il manque l'équivalent *PlaceAruco***
- *PickAruco* permet de repérer le QR code de l'objet avec PoseStamped, puis de lancer la tâche de *pick* avec les mouvements suivants : placement du bras au dessus de la table, récupération de la position de l'objet, attrapage de l'objet, lever du bras, retour à la position au dessus de la table, retour à la position *home*.

## Bilan sur les fichiers manquant
Il semblerait qu'il manque principalement la classe PlaceAruco dans le fichier *pick_client.py* afin de gérer le placement de l'objet. Peut-être aussi des fichiers de configuration. Renommer *pick_client.py* ou changer une partie du code pour créer *place_client.py*.
Ces fichiers ont été pris du tutoriel de *tiago_pick_demo* fourni pour Tiago sur Gazebo (*pick_and_place_server.py* n'a pas été changé). *pick_client.py* a été changé : ont été ajouté un passage par une position d'approche avant d'attraper la balle et un retour à la position *home* une fois la balle attrapée (au lieu d'un retour à la position d'attrape).   
Les fichiers *motion_planning_server.py* et *node_prise.py* ont été créés par les étudiants de l'an dernier mais il est difficile de savoir à quoi ils servent.  


