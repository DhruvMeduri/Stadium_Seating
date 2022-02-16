# ALGORITHM COMPARISON GRAPHS ( Max Cluster Rectangle ) :

from max_cluster_rectangle import alg_class
from max_cluster_rectangle import config_shape
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pathlib import Path  #to give relative path for fil instead of full absolute path from drive letter
import numpy as np
from max_cluster_rectangle import addon
from baseline import base_line
from block import Block_algo
    
# Plots the percentage of filled seats aganist varying square dimensions keeping the dimension of the max cluster rectangle constant. This function compares all 3 algorithms: Greedy, Baseline & Block.
def square_comparison_dimension():
    msize = int(input("Enter max dimension: "))
    mlength = int(input("Enter max length: "))
    mbreadth = int(input("Enter max breadth: "))
    alg_list=[]
    base_list=[]
    block_list = []
    x_list = []
    shapes = config_shape.seq(mlength,mbreadth)
    configs = config_shape.printconfig(shapes)  
    for i in range(3,msize+1,3):
      obj = alg_class.compute_arrangement(i,mlength,mbreadth)
      obj.total = len(obj.uncovered)
      obj.add_final(configs)
      alg_ratio = (obj.occ/obj.total)*100
      alg_list.append(alg_ratio)
      base_ratio = base_line.baseline(i,i,mlength*mbreadth)
      base_list.append(base_ratio)
      block_ratio = Block_algo.block_algo(i,i,mlength*mbreadth)
      block_list.append(block_ratio)
      x_list.append(i)
      print(i)
    #print(alg_list)
    plt.title("Max Rectangle = ("+ str(mlength)+','+str(mbreadth)+")",fontsize=25)
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
    
# Plots the percentage of filled seats aganist varying diagonal length of the diamond keeping the dimension of the max cluster rectangle constant. This function compares Greedy & Baseline algorithms. 
def diamond_comparison_dimension():
    msize = int(input("Enter max dimension: "))
    length = int(input("Enter cluster length: "))
    breadth = int(input("Enter cluster breadth: "))
    alg_list=[]
    base_list=[]
    x_list = []
    shapes = config_shape.seq(length,breadth)
    configs = config_shape.printconfig(shapes) 
    for i in range(3,msize+1):
      obj = alg_class.compute_arrangement(i,length,breadth)
      obj.uncovered = addon.diamond_shape(obj.uncovered,i)
      obj.wasted = addon.diamond_waste(obj.wasted,i)
      obj.init_covered = obj.wasted
      obj.total = len(obj.uncovered)
      obj.add_final(configs)
      alg_ratio = (obj.occ/obj.total)*100
      alg_list.append(alg_ratio)
      base_ratio = base_line.baseline_diamond(i,length*breadth)
      base_list.append(base_ratio)
      x_list.append(i)
      print(i)
    print(alg_list)
    plt.title("Max Rectangle = ("+ str(length)+','+str(breadth)+")",fontsize=25)
    plt.xlabel("Diagnal of diamond",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(x_list,fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list,alg_list,marker='X')
    plt.plot(x_list,base_list,color='red',marker='X')
    plt.legend(('Greedy', 'Baseline'),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    plt.axis([0,40,0,100])
    plt.show()
    
# Plots the percentage of filled seats aganist varying dimensions of max cluster rectangle keeping the dimension of the rectangle constant. This function compares all 3 algorithms: Greedy, Baseline & Block.
def rectangle_comparison_family():
    l = int(input("Enter Length of Rectangle: "))
    b = int(input("Enter breadth of rectangle: "))
    size = max([l,b])
    alg_list=[]
    base_list=[]
    block_list = []
    x_list1 = ['(2,3)','(4,2)','(3,3)','(2,5)','(4,3)','(7,2)']
    x_list = [[2,3],[4,2],[3,3],[2,5],[4,3],[7,2]]
    for i in x_list:
      obj = alg_class.compute_arrangement(size,i[0],i[1])
      shapes = obj.seq(i[0],i[1])
      configs = obj.printconfig(shapes)
      obj.uncovered = addon.rectangle_shape(obj.uncovered,size,l,b)
      obj.wasted = addon.rectangle_waste(obj.wasted,size,l,b)
      obj.init_covered = obj.wasted
      obj.total = len(obj.uncovered)
      obj.add_final(configs)
      alg_ratio = (obj.occ/obj.total)*100
      alg_list.append(alg_ratio)
      base_ratio = base_line.baseline(l,b,i[0]*i[1])
      base_list.append(base_ratio)
      block_ratio = Block_algo.block_algo(l,b,i[0]*i[1])
      block_list.append(block_ratio)
      print(i)
    print(alg_list)
    plt.title("Rectangle = ("+ str(l)+','+str(b)+")",fontsize=25)
    plt.xlabel("Max Cluster Rectangle",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list1,alg_list,marker='X')
    plt.plot(x_list1,base_list,color='red',marker='X')
    plt.plot(x_list1,block_list,color='green',marker='X')
    plt.legend(('Greedy', 'Baseline', 'Block'),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    #plt.axis([0,10,0,100])
    plt.show()
    
# # Plots the percentage of filled seats aganist varying dimensions of max cluster rectangle keeping the dimension of the square and the hole constant. This function compares Greedy & Baseline algorithms. 
def hole_comparison_family():
    size = int((input("Enter size of big square")))
    l = int(input("Enter Length of hole: "))
    b = int(input("Enter breadth of hole: "))    
    alg_list=[]
    base_list=[]
    x_list1 = ['(2,3)','(4,2)','(3,3)','(2,5)','(4,3)','(7,2)']
    x_list = [[2,3],[4,2],[3,3],[2,5],[4,3],[7,2]]
    for i in x_list:
      obj = alg_class.compute_arrangement(size,i[0],i[1])
      shapes = obj.seq(i[0],i[1])
      configs = obj.printconfig(shapes)
      obj.uncovered = addon.hole_shape(obj.uncovered,size,l,b)
      obj.wasted = addon.hole_waste(obj.wasted,size,l,b)
      obj.init_covered = obj.wasted
      obj.total = len(obj.uncovered)
      obj.add_final(configs)
      alg_ratio = (obj.occ/obj.total)*100
      alg_list.append(alg_ratio)
      base_ratio = base_line.baseline_hole(size,l,b,i[0]*i[1])
      base_list.append(base_ratio)
      print(i)
    print(alg_list)
    plt.title("Square dimension = " + str(size)+ "Hole Dimension = " + "("+ str(l)+','+str(b)+")",fontsize=25)
    plt.xlabel("Cluster rectangle",fontsize=18)
    plt.ylabel("% filled",fontsize=18)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(x_list1,alg_list,marker='X')
    plt.plot(x_list1,base_list,color='red',marker='X')
    plt.legend(('Greedy', 'Baseline'),loc='upper right', shadow=True,borderpad=1,fontsize=15)
    plt.axis([0,10,0,100])
    plt.show()
