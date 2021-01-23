# projet-integration-sri-2020-2021
Projet d'intégration ROS SRI 2020 2021

# Organization:

Planification de tâches: François Mahe
Package: tiago_demo_sri_g2_2021
	En l'état l'executable tiago_demo permet de lancer sur le robot une séquence plannifiée devant mener le robot a 
	se localiser puis naviger vers le lieux de saisit de l'objet, saisir l'objet, naviguer vers le lieux de dépose 
	de l'objet pour	y déposer l'objet.
	L'ordonnemencement est actuellement en echec car le robot ne parvient pas encore a se localiser convenablement, 
	ce qui met la tâche de navigation en defaut sur le robot.
	L'ordonnancement, s'appuit sur les actions du packet ROS actionLib. Chaque groupe a develloper sa partie de manière
	a fournir une action, instanciée par un serveur. tiago_demo declanche donc des clients, qui viennent commander des 
	actions au divers servers afin de mener a bien la mission de pick and place du robot. L'ordonnancement est modélisé
	par une machine a état standard.
	

Perception: Moufdi

Simulation: 
@Arnaud-Lucas
@XavierBaby
@NicoBGithub

Navigation:
Marc Girard --> commit au nom de MarcGirard et Etudiant. 
	V1 node move_to_goal.py
	V1 node start_localisation.py 
	Mise en place de la map salle groix dans rviz
	Merge entre le travail de l'équipe simulation sur gazebo et ce que j'ai fait sur rviz + fichier update_rviz_map.py
	Tests navigation
	Videos demo à télécharger: https://filesender.renater.fr/?s=download&token=f393ab8e-c359-439c-9774-c3fc7fe0dc03
Axel porcino
Sylvain Cadel

Axel Porcino--> commit au nom de Axelito95.
	creation server-action pour mote_to_goal_py
	creation server-action pour start_localisation.py
	test Navigation sur la simulation de l'equipe simulation plus la carte slam realisè avec marc et sylvain.

Nicolas Boirel --> commit au nom de NicoBGithub.
	Equipe simulation
	Ajout de la cellule robotique dans le modèle 3D de la salle
	Amélioration de la modélisation de la salle
	Création des modèles 3D allégés de la cellule seule et des aiguillages, pour un ajout futur dans la simulation Gazebo.

Plannification de mouvement
Florent Labrune --> package : motion_planning
	Etude du code tiago_pick_demo
	Definition de l'architecture Action Server/Client
	Etude des points d'approches pour optimiser le motion planning
	Je n'ai fais aucun commit mais j'ai beaucoup participé à ceux de selimmch

Laura Martinez --> 
	Etude de la démo Tiago de plannification de mouvement "tiago_pick_demo".
	Tentative d'installation de la démo sur pc perso pendant toute la semaine sans succès, donc pas de commit effectués.
	Support pour l'adaptation de la démo dans notre cas d'utilisation (participation aux commits de selimmch). 
	
Lila David --> package : motion_planning
	Etude de la démonstration Tiago de plannification de mouvements avec le tutorial MoveIt : "tiago_pick_demo"
	Aide pour l'utilisation et la modification de cette démo pour notre problématique (participation aux commits de selimmch).
	Compétences acquises : meilleure compréhension de l'architecture d'un projet ROS (notamment avec l'utilisation de métapackages), meilleure compréhension et 		utilisation de l'outil git.  
