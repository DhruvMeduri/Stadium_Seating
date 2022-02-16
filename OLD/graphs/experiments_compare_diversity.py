# DIVERSITY GRAPHS :

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 'plot_diversity_comparison' plots the MEAN family size chosen for each square dimension in both the cases : All configs and Max Cluster Rectangle .

def plot_diversity_comparison():

    msize = int(input("Enter max dimension: "))
    mlength = int(input("Enter max length: "))
    mbreadth = int(input("Enter max breadth: "))
    mcr_diversity=[]
    x_list = []
    
    from max_cluster_rectangle import alg_class
    from max_cluster_rectangle import config_shape
    from max_cluster_rectangle import addon
    shapes = config_shape.seq(mlength,mbreadth)
    configs = config_shape.printconfig(shapes)      
    for i in range(3,msize+1):
      obj = alg_class.compute_arrangement(i,mlength,mbreadth)
      obj.total = len(obj.uncovered)
      obj.add_final(configs)
      mean_div = obj.mean()
      mcr_diversity.append(mean_div)
      x_list.append(i)
    
    from all_config import alg_class
    from all_config import config_shape
    from all_config import addon
    all_config_diversity = []    
    shapes = config_shape.seq(mlength*mbreadth)
    configs = config_shape.printconfig(shapes)
    for i in range(3,msize+1):
      obj = alg_class.compute_arrangement(i,mlength*mbreadth)
      obj.total = len(obj.uncovered)
      obj.add_final(configs)
      alg_ratio = obj.mean()
      all_config_diversity.append(alg_ratio)

    
    plt.title("Max Rectangle = ("+ str(mlength)+','+str(mbreadth)+")",fontsize=25)
    plt.xlabel("Dimension of Square",fontsize=18)
    plt.ylabel("Mean Family Size",fontsize=18)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,mcr_diversity,marker='X')
    plt.plot(x_list,all_config_diversity,marker='X',color='red')
    plt.legend(('Max Cluster Rect', 'All Configs'),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    
    plt.show() 