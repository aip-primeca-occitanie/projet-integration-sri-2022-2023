# Liste des contributions par auteurs:

Mouliets Cédérick : 

Remplacement du dossier tiago_pick_simulation en un nouveau package sri_tiago_pick et renommage des imports dans les fichiers du package remplacé. Ajout du cube dans la simulation groix_porquerolles.world. Adaptation de la position du robot pour qu'il soit devant une des tables sur lequel le cube est posé afin qu'il puisse le détecter. Adaptation de la démo du pick de tiago dans la simulation (voir README.md dans la branche principale pour lancer cette démo et le README.md du package sri_tiago_pick pour lire sa description).


Delauzun Rémi et Bizet Raphaël :
--> commit aux noms de strengthless-razzia & remidelz & marcgirard & lilia00

Implémentation de multi-tiago en simulation. Adaptation des fichiers .launch existants pour prendre en compte une nouvelle map : la salle groix et porquerolle. Deux tiago sont placés dans la salle avec une position initiale codé en dur. (voir README.md dans la branche principale pour lancer cette démo et le README.md du package mulitiago pour lire sa description)

Clément Petit et Alexandre Baures
--> commit aux noms de ClementPagran et abaures

Focalisation du travail sur la partie place du pick_and_place. Réalisation du package tiago_place
On a commencé par vouloir changer le fichier pick_and_place.py en modifiant la partie pick pour realiser un place, cette opération nous a permis de mieux comprendre l'organisation du code du tiago_pick_demo mais c'est avéré trop compliqué a mettre en place.
On a ensuite modifié le fichier pick_client.py pour réaliser seulement la partie place en supprimant les operations de pick. Une erreur de group_name nous a empeché de réaliser l'opération, malheuresement le message d'erreur etait inexistant ou incompréhensible. Nous avons donc décidé d'aller directemnt installer et compiler le package moveit utilisé pour cette démo pour modifier et comprendre le message d'erreur et ainsi pouvoir resoudre le problème.
On s'est rendu compte que pour que le place fonctionne, il est necessaire d'avoir réalisé l'operation pick qui associe l'objet à prendre au robot. Si cette étape n'est pas realisé, l'operation place plante.
