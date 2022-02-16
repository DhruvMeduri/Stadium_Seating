# this file defines the class required for the running the greedy algorithm.
import compute_configs
import set_universe
#import addon
import numpy as np
from os import system
import time

class compute_arrangement():

  def __init__(self,size,mfamily):
      self.init_covered = set()
      self.occ = 0
      self.total = 0
      self.sets = []
      self.size = size
      self.mfamily = mfamily
      self.matrix = np.zeros((size,size),dtype = 'U')
      for i in range(size):
          for j in range(size):
            self.matrix[i][j] = '0'
      self.occupied = set()
      self.wasted = set()
      self.uncovered = set()
      for i in range(size*size):
          self.uncovered.add(i)


  def printconfig(self):
      # check config_shape.py
      con = compute_configs.compute_configs(self.mfamily)
      return con

  def allsets(self,configs):
    # check set_universe.py and addon.py
    tconfig = set_universe.allsets(self.size,configs)
    #tconfig = addon.remove_irrelevant_sets(self.init_covered,tconfig) # big change in code keep in mind for error
    return tconfig

  def compute_ratio(self,ele):
    # Input: The set along with the current uncovered seats
    # Output: returns the required ratio for every set
    ratio = (len(ele[1]& self.uncovered))/((len(ele[1]& self.uncovered))+(len(ele[0]& self.uncovered)))
    return ratio


  def add_final(self,configs):
    # Input: The set of configurations and the dimension of the theatre/stadium. This is the implementation of the alg described in the paper.
    # Output: Final arrangement after running the greedy.
    self.sets = self.allsets(configs)
    #print(self.sets)
    while len(self.uncovered)>0:
      mini=[]
      rat = 1
      for i in self.sets:
        if (i[1]& self.uncovered) | (i[0]& self.uncovered) != set():
          ele_ratio = self.compute_ratio(i)
          if ele_ratio <= rat:
            rat = ele_ratio
            mini = i
      #print((mini[1] & self.uncovered) | (mini[0] & self.uncovered))
      self.occupied = self.occupied|(mini[0] & self.uncovered)
      self.wasted = self.wasted|(mini[1] & self.uncovered)
      self.uncovered = self.uncovered - mini[0] - mini[1]
      #print(mini)
      #print(self.uncovered)
      #ch = input("\nnext")
    for i in range(self.size*self.size):
       if i in self.occupied:
          self.occ = self.occ + 1
          self.matrix[int(i/self.size)][i % self.size] = '1'
       if i in self.wasted:
          self.matrix[int(i/self.size)][i % self.size] = ' '
    # To compute the performance
    count = 0
    for r in range(self.size):
       for c in range(self.size):
          if self.matrix[r][c] == '1':
              count = count+1
    return((100*count)/(self.size*self.size))


  def print_format(self):
    count = 0
    for r in range(self.size):
       for c in range(self.size):
          if self.matrix[r][c] == '1':
              count = count+1
          print(self.matrix[r][c],end = '   ')
       print('\n')

#start = time.time()
#obj = compute_arrangement(10,5)
#configs = obj.printconfig()
#print("Occupance %",obj.add_final(configs))
#end = time.time()
#obj.print_format()
#print("Runtime: ", end-start)
