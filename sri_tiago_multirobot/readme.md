# Documentation Multi Robot

Pour pouvoir connecter plusieur robot, nous allons devoir installer le package ros [multimaster_fkie](http://wiki.ros.org/multimaster_fkie/Tutorials/Setup%20a%20ROS%20master%20synchronization) qui va nous permettre de synchonisé les topic entre les roscore. 

## installation

Connecter au robot, et en mode administrateur, installer pip si il ne l'ai pas déjà, puis le module gRPC avec la commande suivante : 

`pip install grpc`

par la suite, vous devez suivre le tuto pour compilé localement le code source du packet. pour se faire,vous devez créer un workspace pour y mettre le code source, puis compiler le packet graçe au commande suivant : 

`cd catkin_ws/src`  
`git clone https://github.com/fkie/multimaster_fkie.git multimaster `  
`rosdep update`  
`rosdep install -i --as-root pip:false --reinstall --from-paths multimaster`  
`catkin build fkie_multimaster`  

si vous voulez plusieur roscore sur différent robot, vous devez 

une fois installez sur les deux robot, vous pouvez lancez le packet sur les deux robot : 

`rosrun master_discovery_fkie master_discovery`

cette commmande permet de lancer la partie du packet qui va faite la découverte du réseau pour trouvé les autre roscore.  

`rosrun master_sync_fkie master_sync`

cette commande permet de synchronisé les master (donc tout les noeud seront visible sur les 2 roscore) 

pour synchronisé une partie uniquement des topics, vous pouvez utilisé la commande suivante en remplacant ce qu'il y a dans les crochet par votre liste de topic :

`rosrun master_sync_fkie master_sync _sync_topics:=["/test/topic"]`