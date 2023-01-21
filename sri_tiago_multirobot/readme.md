# Documentation Multi Robot

Pour pouvoir connecter plusieurs robots, nous allons devoir installer le package ros [multimaster_fkie](http://wiki.ros.org/multimaster_fkie/Tutorials/Setup%20a%20ROS%20master%20synchronization) qui va nous permettre de synchoniser les topics entre les roscore. 

## installation

Se connecter au robot, et en mode administrateur installer pip si il ne l'est pas déjà, puis le module gRPC avec la commande suivante : 

`pip install grpc`

Pour la suite, vous devez suivre le tuto pour compiler localement le code source du paquet. pour se faire, vous devez créer un workspace pour y mettre le code source, puis compiler le paquet grâce au commande suivant : 

`cd catkin_ws/src`  
`git clone https://github.com/fkie/multimaster_fkie.git multimaster `  
`rosdep update`  
`rosdep install -i --as-root pip:false --reinstall --from-paths multimaster`  
`catkin build fkie_multimaster`  

Si vous voulez plusieurs roscore sur différents robots, vous devrez activer 2 fonctionnalités grâce au terminal

`sh -c "echo 1 >/proc/sys/net/ipv4/ip_forward"`  
`sh -c "echo 0 >/proc/sys/net/ipv4/icmp_echo_ignore_broadcasts"`

## Utilisation 

Une fois installé sur les deux robots, vous pouvez lancer le paquet sur les deux robots :

`rosrun fkie_master_discovery master_discovery`

Cette commmande permet de lancer la partie du paquet qui va faire la découverte du réseau pour trouver les autres roscore.  

`rosrun master_sync_fkie master_sync`

Cette commande permet de synchroniser les master (donc tout les noeuds seront visible sur les 2 roscore) 

Pour synchroniser un certain nombre des topics, vous pouvez utiliser la commande suivante en remplacant ce qu'il y a dans les crochets par votre liste de topic :

`rosrun  fkie_master_sync master_sync _sync_topics:=["/test/topic"]`

Cette commande à été testée avec succès sur des PC portables mais les tests n'ont pas pu être menés correctement sur les TIAGO par manque de temps

( Pour les PC le process d'installation était différent, les commandes sont du types master_xxx_fkie au lieu de fkie_master_xxx )

