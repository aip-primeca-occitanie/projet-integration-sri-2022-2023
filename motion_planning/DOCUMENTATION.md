# Documentation de la partie *motion_planning*

## Fichiers *.launch*
 `pick_simulation.launch` : permet de créer le robot et son environnement dans Gazebo, avec un appel au fichier *.launch* dédié fourni par Tiago (fichier `tiago_gazebo.launch` présent quelque part dans le dossier *tiago_public_ws*). Dans les paramètres utilisés on a notamment le type du robot (ici, *steel*, donc avec une pince) et son environnement (ici *tabletop_cube*, environnement prédéfini disponible dans *tiago_public_ws/src/pal_gazebo_worlds/worlds/* et qui utilise des éléments qui se trouvent dans *tiago_public_ws/src/pal_gazebo_worlds/models/*).     
 
 `pick_demo.launch` : ce fichier a deux rôles : créer le visionnage RVIZ et lier les fichiers pour le Pick & Place à la simulation Gazebo.   
 Les fichiers importants appelés sont *config/pick_motions.yaml* et ceux permettant de créer le node *pick_and_place_serveur*, *pick_and_place_server.py* et *config/pick_and_place_params.yaml*.   
 Enfin, deux nodes sont créés pour les manipulations : *pick_client* et *place_client*, appelant *pick_client.py* et *place_client.py*; ainsi que leurs modélisations sur RVIZ gérées par *config/rviz/tiago_pick_demo.rviz*.   
 **Restent à faire : *pick_client.py*, *config/rviz/tiago_place_demo.rviz* et potentiellement *config/place_motions.yaml*** (en gros tout ce qui permet de créer et exécuter le node *place_client*).   
