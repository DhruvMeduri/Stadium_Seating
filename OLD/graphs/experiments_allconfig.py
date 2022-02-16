# ALGORITHM COMPARISON GRAPHS ( All Configurations ) :

from all_config import alg_class
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pathlib import Path  
import numpy as np

from all_config import addon
from all_config import config_shape
from baseline import base_line
from block import Block_algo

# Plots the percentage of filled seats aganist varying square dimensions keeping the max cluster size constant.This function compares Block & Baseline algorithms.
def block_comparison_dimension():
    msize = int(input("Enter max dimension(>3): "))
    mcluster = int(input("Enter max cluster size: "))
    base_list=[]
    block_list=[]
    x_list = []
    
    for i in range(3,msize+1,3):
      base_ratio = base_line.baseline(i,i,mcluster)
      block_ratio = Block_algo.block_algo(i,i,mcluster)
      block_list.append(block_ratio)
      base_list.append(base_ratio)
      x_list.append(i)
      
      
    plt.title("Max cluster Size = "+ str(mcluster),fontsize=25)
    plt.xlabel("Dimension of Square",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(x_list,fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,block_list,marker='X')
    plt.plot(x_list,base_list,color='red',marker='X')
    plt.legend(('Block', 'Baseline' ),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    plt.axis([0,60,0,100])
    plt.show()

# Plots the percentage of filled seats aganist max varying cluster size keeping the dimensions of the rectangle constant.This function compares Block & Baseline algorithms.
def block_rectangle_comparison_csize():
    b = int(input("Enter the no of rows: "))
    l = int(input("Enter the no of columns: "))
    msize = max([l,b])
    mcluster = int(input("Enter maximum max cluster size: "))
    block_list = []
    alg_list=[]
    base_list=[]
    x_list = []
    
    for i in range(1,mcluster+1):
      base_ratio = base_line.baseline(b,l,i)
      base_list.append(base_ratio)
      block_ratio = Block_algo.block_algo(b,l,i)
      block_list.append(block_ratio)
      x_list.append(i)
      
    plt.title("Dimension of Rectangle = "+str(b)+" X "+str(l),fontsize=25)
    plt.xlabel("Max Cluster Size",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(x_list,fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,block_list,marker='X')
    plt.plot(x_list,base_list,color='red',marker='X')
    plt.legend(('Block', 'Baseline' ),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    plt.axis([0,30,0,100])
    
    plt.show()

# Plots the percentage of filled seats aganist varying square dimensions keeping the max cluster size constant. This function compares all 3 algorithms: Greedy, Baseline & Block.
def square_comparison_dimension():

    msize = int(input("Enter max dimension(>3): "))
    mcluster = int(input("Enter max cluster size: "))
    alg_list=[]
    base_list=[]
    block_list=[]
    x_list = []
    shapes = config_shape.seq(mcluster)
    configs = config_shape.printconfig(shapes) 
    
    for i in range(3,msize+1,3):
      obj = alg_class.compute_arrangement(i,mcluster)
      obj.total = len(obj.uncovered)
      obj.add_final(configs)
      alg_ratio = (obj.occ/obj.total)*100
      alg_list.append(alg_ratio)
      base_ratio = base_line.baseline(i,i,mcluster)
      block_ratio = Block_algo.block_algo(i,i,mcluster)
      block_list.append(block_ratio)
      base_list.append(base_ratio)
      x_list.append(i)
    
    plt.title("Max cluster Size = "+ str(mcluster),fontsize=25)
    plt.xlabel("Dimension of Square",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(x_list,fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,alg_list,marker='X')
    plt.plot(x_list,base_list,color='red',marker='X')
    plt.plot(x_list,block_list,color='green',marker='X')
    plt.legend(('Greedy', 'Baseline', 'Block'),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    plt.axis([0,50,0,100])
    plt.show()
    
# Plots the percentage of filled seats aganist varying the diagonal length of the diamond keeping the max cluster size constant. This function compares Greedy & Baseline algorithms.
def diamond_comparison_dimension():

    msize = int(input("Enter max dimension(>3): "))
    mcluster = int(input("Enter max cluster size: "))
    alg_list=[]
    base_list=[]
    x_list = []
    shapes = config_shape.seq(mcluster)
    configs = config_shape.printconfig(shapes) 
    
    for i in range(3,msize+1):
      obj = alg_class.compute_arrangement(i,mcluster)
      obj.uncovered = addon.diamond_shape(obj.uncovered,i)
      obj.wasted = addon.diamond_waste(obj.wasted,i)
      obj.init_covered = obj.wasted
      obj.total = len(obj.uncovered)
      obj.add_final(configs)
      alg_ratio = (obj.occ/obj.total)*100
      alg_list.append(alg_ratio)
      base_ratio = base_line.baseline_diamond(i,mcluster)
      base_list.append(base_ratio)
      x_list.append(i)
   
    plt.title("Max cluster Size = "+ str(mcluster),fontsize=25)
    plt.xlabel("Size of Diagonal (Diamond like arrangement)",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,alg_list,marker='X')
    plt.plot(x_list,base_list,color='red',marker='X')
    plt.legend(('Greedy', 'Baseline'),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    plt.axis([0,60,0,100])
    plt.show()
    
# Plots the percentage of filled seats aganist varying max cluster size keeping the dimension of the square constant. This function compares all 3 algorithms: Greedy, Baseline & Block.
def square_comparison_csize():

    msize = int(input("Enter dimension: "))
    mcluster = int(input("Enter maximum max cluster size: "))
    alg_list=[]
    base_list=[]
    block_list = []
    x_list = []
    
    for i in range(1 , mcluster + 1):
      obj = alg_class.compute_arrangement(msize,i)
      obj.total = len(obj.uncovered)
      shapes = config_shape.seq(i)
      configs = config_shape.printconfig(shapes)
      obj.add_final(configs)
      alg_ratio = (obj.occ/obj.total)*100
      alg_list.append(alg_ratio)
      base_ratio = base_line.baseline(msize,msize,i)
      base_list.append(base_ratio)
      block_ratio = Block_algo.block_algo(msize,msize,i)
      block_list.append(block_ratio)
      x_list.append(i)
  
    plt.title("Max cluster Size = "+ str(mcluster),fontsize=25)
    plt.xlabel("Dimension of Square",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,alg_list,marker='X')
    plt.plot(x_list,base_list,color='red',marker='X')
    plt.plot(x_list,block_list,color='green',marker='X')
    plt.legend(('Greedy', 'Baseline', 'Block'),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    #plt.axis([0,15,0,100])
    plt.show()
    
# Plots the percentage of filled seats aganist varying max cluster size keeping the diagonal length of the diamond constant. This function compares Greedy & Baseline algorithms.
def diamond_comparison_csize():

    msize = int(input("Enter dimension: "))
    mcluster = int(input("Enter maximum max cluster size: "))
    alg_list=[]
    base_list=[]
    x_list = []
    
    for i in range(1,mcluster+1):
      obj = alg_class.compute_arrangement(msize,i)
      obj.uncovered = addon.diamond_shape(obj.uncovered,msize)
      obj.wasted = addon.diamond_waste(obj.wasted,msize)
      obj.init_covered = obj.wasted
      obj.total = len(obj.uncovered)
      shapes = config_shape.seq(i)
      configs = config_shape.printconfig(shapes)
      obj.add_final(configs)
      alg_ratio = (obj.occ/obj.total)*100
      alg_list.append(alg_ratio)
      base_ratio = base_line.baseline_diamond(msize,i)
      base_list.append(base_ratio)
      x_list.append(i)
  
    plt.title("Diagonal Size of Diamond = "+ str(msize),fontsize=25)
    plt.xlabel("Size of Diagonal (Diamond like arrangement)",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,alg_list,marker='X')
    plt.plot(x_list,base_list,color='red',marker='X')
    plt.legend(('Greedy', 'Baseline'),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    plt.axis([0,60,0,100])
    plt.show()
    
# Plots the percentage of filled seats aganist varying max cluster size keeping the dimension of the square and the hole size constant. This function compares Greedy & Baseline algorithms.
def hole_comparison_csize():

    msize = int(input("Enter dimension: "))
    le = int(input("Enter length of hole: "))
    br = int(input("Enter breadth of hole: "))
    mcluster = int(input("Enter maximum max cluster size: "))
    alg_list=[]
    base_list=[]
    x_list = []
    
    for i in range(1,mcluster+1):
      print(i)
      obj = alg_class.compute_arrangement(msize,i)
      obj.uncovered = addon.hole_shape(obj.uncovered,msize,le,br)
      obj.wasted = addon.hole_waste(obj.wasted,msize,le,br)
      obj.init_covered = obj.wasted
      obj.total = len(obj.uncovered)
      shapes = config_shape.seq(i)
      configs = config_shape.printconfig(shapes)
      obj.add_final(configs)
      alg_ratio = (obj.occ/obj.total)*100
      alg_list.append(alg_ratio)
      base_ratio = base_line.baseline_hole(msize,br,le,i)
      base_list.append(base_ratio)
      x_list.append(i)

    plt.title("Square Dimension : "+ str(msize)+' and Hole dimension :'+str(le)+'x'+str(br),fontsize=25)
    plt.xlabel("Max Cluster Size",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,alg_list,marker='X')
    plt.plot(x_list,base_list,color='red',marker='X')
    plt.legend(('Greedy', 'Baseline'),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    plt.axis([0,60,0,100])
    plt.show()
    
# Plots the percentage of filled seats aganist varying max cluster size keeping the dimensions of the rectangle constant. This function compares all 3 algorithms: Greedy, Baseline & Block.
def rectangle_comparison_csize():

    b = int(input("Enter the no of rows: "))
    l = int(input("Enter the no of columns: "))
    msize = max([l,b])
    mcluster = int(input("Enter maximum max cluster size: "))
    block_list = []
    alg_list=[]
    base_list=[]
    x_list = []
    
    for i in range(1,mcluster+1):
      obj = alg_class.compute_arrangement(msize,i)
      obj.uncovered = addon.rectangle_shape(obj.uncovered,msize,l,b)
      obj.wasted = addon.rectangle_waste(obj.wasted,msize,l,b)
      obj.init_covered = obj.wasted
      obj.total = len(obj.uncovered)
      shapes = config_shape.seq(i)
      configs = config_shape.printconfig(shapes)
      obj.add_final(configs)
      alg_ratio = (obj.occ/obj.total)*100
      alg_list.append(alg_ratio)
      base_ratio = base_line.baseline(b,l,i)
      base_list.append(base_ratio)
      block_ratio = Block_algo.block_algo(b,l,i)
      block_list.append(block_ratio)
      x_list.append(i)
  
    plt.title("Dimension of Rectangle = "+str(b)+" X "+str(l),fontsize=25)
    plt.xlabel("Max Cluster Size",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(x_list,fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,alg_list,marker='X')
    plt.plot(x_list,base_list,color='red',marker='X')
    plt.plot(x_list,block_list,color='green',marker='X')
    plt.legend(('Greedy', 'Baseline', 'Block'),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    #plt.axis([0,10,0,100])
    plt.show()
    
# Plots the mean of the cluster sizes chosen aganist the dimension of the corresponding square.
def plot_diversity():
    msize = int(input("Enter max dimension(>3): "))
    mcluster = int(input("Enter max cluster size: "))
    alg_list=[]
    x_list = []
    shapes = config_shape.seq(mcluster)
    configs = config_shape.printconfig(shapes)                     
    for i in range(3,msize+1):
      obj = alg_class.compute_arrangement(i,mcluster)
      obj.total = len(obj.uncovered)
      obj.add_final(configs)
      alg_ratio = obj.mean()
      alg_list.append(alg_ratio)
      x_list.append(i)
    
    plt.title("Max cluster Size = "+ str(mcluster),fontsize=25)
    plt.xlabel("Dimension of Square",fontsize=18)
    plt.ylabel("Mean Family Size",fontsize=18)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,alg_list,marker='X')
    #plt.axis([0,60,0,100])
    plt.show()

