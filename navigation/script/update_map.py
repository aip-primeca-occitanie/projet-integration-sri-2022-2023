import os

os.system("cp /home/etudiant/tiago_public_ws/src/projet-integration-sri-2020-2021/navigation/data/salle_groix $HOME/.pal/tiago_maps/configurations")
os.system("rosservice call /pal_map_manager/change_map \"input: \'salle_groix\'\"")