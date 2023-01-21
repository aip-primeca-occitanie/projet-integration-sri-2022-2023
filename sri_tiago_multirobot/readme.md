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

si vous voulez plusieurs roscore sur différents robots, vous devez activer 2 fonctionalité grâce au terminal

`sh -c "echo 1 >/proc/sys/net/ipv4/ip_forward"`  
`sh -c "echo 0 >/proc/sys/net/ipv4/icmp_echo_ignore_broadcasts"`

## utilisation 

une fois installez sur les deux robot, vous pouvez lancez le packet sur les deux robot : 

`rosrun fkie_master_discovery master_discovery`

cette commmande permet de lancer la partie du packet qui va faite la découverte du réseau pour trouvé les autre roscore.  

`rosrun master_sync_fkie master_sync`

cette commande permet de synchronisé les master (donc tout les noeud seront visible sur les 2 roscore) 

pour synchronisé une partie uniquement des topics, vous pouvez utilisé la commande suivante en remplacant ce qu'il y a dans les crochet par votre liste de topic :

`rosrun  fkie_master_sync master_sync _sync_topics:=["/test/topic"]`

cette commande à était testé avec succées sur des PC portable mais les teste non pas pue être mener correctement sur les TIAGO par manque de temps

