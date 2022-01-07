# Documentation de la partie *motion_planning*

## Fichiers *.launch* (dossier /launch)
 `pick_simulation.launch` : permet de créer le robot et son environnement dans Gazebo, avec un appel au fichier *.launch* dédié fourni par Tiago (fichier `tiago_gazebo.launch` à l'origine présent quelque part dans le dossier *tiago_public_ws*, mais maintenant fourni en version modifiée, voir plus bas). Dans les paramètres utilisés on a notamment le type du robot (ici, *steel*, donc avec une pince) et son environnement (ici *tabletop_cube*, environnement prédéfini disponible dans *worlds/tabletop_cube.world*, version modifiée d'un fichier originellement présent dans *tiago_public_ws/src/tiago_simulation/tiago_gazebo/worlds/*).   
 
 `pick_demo.launch` : ce fichier a deux rôles : créer le visionnage RVIZ et lier les fichiers pour le Pick & Place à la simulation Gazebo.   
Il définit les marqueurs Aruco (QR code) qui devront être repérés et qui serviront pour identifier l'objet à attraper et l'endroit où le poser (nodes appelés *aruco_marker1* (id 582) et *aruco_marker2* (id 666)) (plus d'infos sur ces marqueurs dans la suite de ce document).
Il récupère le fichier *pick_motions.yaml* qui référence des mouvements d'articulations du robot.
Enfin il crée les nodes *pick_and_place_server* et *spherical_service* qui servent aux manipulations de pick & place et qui sont gérés par les fichiers .py du même nom décrits plus bas.

`pick_sri.launch` : similaire à *pick_demo.launch* mais ne gère pas l'affichage RVIZ et lance deux nodes supplémentaires : *motion_planning_server* et *node_prise* basés sur les fichiers *motion_planning_server.py* et *node_prise.py*.   
**Fichier créé par les étudiants SRI de 2020-2021, inutilisé dans la configuration actuelle.**

## Fichiers de scripts *.py* (dossier /scripts)

`pick_and_place_server.py` et `spherical_grasps_server.py` : gèrent la partie serveur du pick & place.   
Permettent de créer les services de pick et de place. Fichiers à l'origine créés pour le tutoriel de pick fourni pour Tiago sur Gazebo, réutilisés tels quels et sans modifications.

`spherical_service.py` : gère la création des nodes */pick_gui* et */place_gui* qui servent à faire les manipulations, et qui sont gérés pas les fichiers *pick_client.py* et *place_client.py*.

`pick_client.py` et `place_client.py` : fichiers gérant les manipulations, tous deux très similaires puisque basés sur le fichier *pick_client.py* récupéré dans le tuto Gazebo. Le code important gérant les mouvements se trouve dans la fonction *pick_aruco* (resp. *place_aruco*). Dans l'ordre des opérations, ce code permet de : mettre le robot en position de sécurité de départ (sauf dans le place où la ligne a été commentée, ce mouvement prenant beaucoup de temps); repérer la position du QR code recherché grâce à Aruco (définis dans *pick_demo.launch* par *aruco_marker1* pour le pick et *aruco_marker2* pour le place); puis à partir du *if*, mouvement du bras pour l'éloigner de la table (uniquement pour *place* pour remplacer la ligne commentée), placement du bras au dessus de la table, mouvement vers la position du QR code (un peu plus bas pour la prise de l'objet, un peu plus haut pour sa dépose), attrapage ou dépose, retour du bras dans une position en hauteur, retour du bras dans sa position "home" de départ.
**Restent (éventuellement) à faire :** tests plus approfondis pour mettre en place des mouvements plus fluides ou avec moins de pirouettes, revérifier les collisions entre les premiers mouvements du robot lors du *place* et la table (dépend de la taille de la table). Les positions pour les mouvements sont à priori définis dans les fichiers du dossier *config*.

`motion_planning_server.py` et `node_prise.py` : fichiers créés par les étudiants de 2020-2021, à priori inutiles.

## Données d'environnement (dossiers *config/*, *data/* et *worlds/*)
Ces dossiers contiennent un ensemble de fichiers permettant de créer l'environnement Gazebo dans lequel évolue le robot. Les fichiers d'origine sont ceux utilisés par le tuto Gazebo et disponibles dans les dossiers de *tiago_public_ws/src/tiago_simulation/tiago_gazebo/*. Ils ont été modifiés pour diminuer la taille de la table sur laquelle est posée l'objet et rajouter un deuxième QR code à l'emplacement de dépose de l'objet voulu. En gros, le fichier *.world* est le fichier "main" et utilise les modèles 3D définis dans le dossier *models/* ainsi que les images représentants le QR code 666 qu'on a ajouté dans le dossier *data/* (celui qui repère l'emplacement de dépose).

## Fichiers de configuration (dossier */config*)
Nous n'avons presque pas touché à ces fichiers, mais à priori ils servent à définir les mouvements que le robot peut faire, avec un nom pour chaque mouvement servant à l'appeler depuis les scripts .py et un ensemble de positions des articulations à atteindre.
**A faire ?** Eventuellement, rajouter des positions pour des mouvements plus fluides ?

## Problèmes à l'exécution
Si vous testez le pick & place avec la méthode dans le README (simulation sous Gazebo et RVIZ), vous aurez certainement régulièrement des problèmes divers et assez aléatoires avec les mouvements du robot, parmi lesquels : collisions avec la table, collisions avec l'objet le faisant tomber (mais le robot croira quand même qu'il l'a attrapé donc ça ne coince pas la manipulation), chute de l'objet depuis la pince (dans les rares cas où il arrive à l'attraper), et quelque fois erreur dans la détection Aruco du deuxième QR code (des fois juste en attendant il finit par le voir, des fois non). Attention, un échec dans la simulation Gazebo ne signifie pas nécessairement que le code est disfonctionnel. Globalement, les simulations Gazebo demandent beaucoup de patience et beaucoup d'essais pour avoir un résultat satisfaisant, c'est comme ça que ça fonctionne apparemment.

Quelques fichiers ne sont pas décrits ici, c'est parce qu'on s'y est pas intéressé.

Notez que des tests en situation réelle ont été faits sur les robots Tiago de l'AIP, et ont parfaitement réussi (des vidéos sont disponibles ici : https://drive.google.com/drive/folders/1LlgIVRgbqHhLe2cCItMGBaBCeMK7cbCX?usp=sharing)

