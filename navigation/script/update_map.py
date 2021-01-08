import os

copy_path = "cp " + args[1] + " $HOME/.pal/tiago_maps/configurations"
os.system(copy_path)
os.system("rosservice call /pal_map_manager/change_map \"input: \'salle_groix\'\"")