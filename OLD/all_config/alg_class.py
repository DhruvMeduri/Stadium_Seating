# this file defines the class required for the running the greedy algorithm.
from all_config import config_shape
from all_config import set_universe
from all_config import addon
import numpy as np
from os import system
from collections import defaultdict

class compute_arrangement():

  def __init__(self,size,mfamily):
      self.init_covered = set()
      self.occ = 0
      self.div = [0 for i in range(mfamily)]
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

  def dupli(self,test_list):
    res = config_shape.dupli(test_list)
    return res

  def seq(self,msize):
    # check config_shape.py
    shapes = config_shape.seq(msize)
    return shapes

  def checkconfig(self,ar,l,b,wastage):
    # check config_shape.py
    k = config_shape.checkconfig(ar,l,b,wastage)
    return k

  def printconfig(self,shapes):
      # check config_shape.py
      con = config_shape.printconfig(shapes)
      return con

  def allsets(self,configs):
    # check set_universe.py and addon.py
    tconfig = set_universe.allsets(self.size,configs)
    tconfig = addon.remove_irrelevant_sets(self.init_covered,tconfig) # big change in code keep in mind for error
    return tconfig

  def compute_ratio(self,ele):
    # Input: The set along with the current uncovered seats
    # Output: returns the required ratio for every set
    ratio = (len(ele[1]& self.uncovered))/((len(ele[1]& self.uncovered))+(len(ele[0]& self.uncovered)))
    return ratio

  def diverse_check(self,se):
    # Input: The chosen set in the given iteration along with the current uncovered seats.
    # Output: Updates the diversity list in every iteration.
    index_list=[]
    for i in se:
        index_list.append(i)

    # This class represents a directed graph using adjacency list representation
    class Graph:

        def __init__(self, vertices):
            # No. of vertices
            self.V = vertices
            self.lst = []
            # default dictionary to store graph
            self.graph = defaultdict(list)


        # function to add an edge to graph
        def addEdge(self, u, v):
            self.graph[u].append(v)

        '''A recursive function to print all paths from 'u' to 'd'.
        visited[] keeps track of vertices in current path.
        path[] stores actual vertices and path_index is current
        index in path[]'''

        def printAllPathsUtil(self, u, d, visited, path):
            #print(u)
            # Mark the current node as visited and store in path
            visited[index_list.index(u)]= True
            path.append(u)

            # If current vertex is same as destination, then print
            # current path[]
            if u == d:
                k = []
                for i in path:
                    k.append(i)

                self.lst.append(k)
                #print(path)

            else:
                # If current vertex is not destination
                # Recur for all the vertices adjacent to this vertex
                for i in self.graph[u]:
                    if visited[index_list.index(i)]== False:
                        self.printAllPathsUtil(i , d , visited, path)

            # Remove current vertex from path[] and mark it as unvisited
            path.pop()
            visited[index_list.index(u)]= False


        # Prints all paths from 's' to 'd'
        def printAllPaths(self, s, d):

            # Mark all the vertices as not visited
            visited =[False]*(self.V)

            # Create an array to store paths
            path = []

            # Call the recursive helper function to print all paths
            self.printAllPathsUtil(s, d, visited, path)

    #Create a graph given in the above diagram

    g = Graph(len(se))
    #print(g.V)
    #print('l,b',l,b)
    for k in index_list:
        i = int(k/self.size)
        j = k % self.size
        if k + self.size in index_list:
           g.addEdge(k, k + self.size)
           #print(k,',',k + self.size)
        if k - self.size in index_list:
           g.addEdge(k, k - self.size)
           #print(k,',',k - self.size)
        if k + 1 in index_list:
           g.addEdge(k , k + 1)
          #print(k,',',k + 1)
        if k - 1 in index_list:
           g.addEdge(k , k -1)
           #print(k,',',k - 1)
    intersection = []
    for i in se & self.uncovered:
        intersection.append(i)
    #print(intersection)
    while intersection != []:
        temp = []
        temp1 = []
        count = 1
        for p in range(1,len(intersection)):
            g.lst=[]
            #print(intersection[0],intersection[p])
            g.printAllPaths(intersection[0],intersection[p])
            #print(g.lst)
            for i in g.lst:
                flag =0
                for j in i:
                    if j not in intersection:
                        flag =1
                        break
                if flag == 0:
                    temp1.append(i)

            g.lst = temp1
            if g.lst == []:
                temp.append(intersection[p])
            else:
                count = count + 1

        intersection = temp
        #print(intersection)
        self.div[count-1] = self.div[count-1] + 1
        #print(temp)
  def mean(self):
      # Input: Diversity list
      # Output: Returns the mean family size of the arrangement
      num = 0
      den = 0
      for i in range(len(self.div)):
          num = num + (i+1)*self.div[i]
          den = den + self.div[i]
      return (num/den)
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
      self.diverse_check(mini[0])
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

  def print_format(self):
    for r in range(self.size):
       for c in range(self.size):
          print(self.matrix[r][c],end = '   ')
       print('\n')
    ch = input("Press enter to continue ")
    system("cls")

  def step_by_step(self,configs):
    # Input: The set of configurations and the dimension of the theatre/stadium
    # Output: Final arrangement after running the greedy but printed after every iteration.
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
      self.diverse_check(mini[0])
      self.occupied = self.occupied|(mini[0] & self.uncovered)
      self.wasted = self.wasted|(mini[1] & self.uncovered)
      self.uncovered = self.uncovered - mini[0] - mini[1]
      #print(mini)
      #print(self.uncovered)
      #ch = input("\nnext")
      print("Chosen Set = ",mini,"\nRatio = ",rat,"Diversity = ",self.div)
      for i in range(self.size*self.size):
         if i in self.occupied:
            self.matrix[int(i/self.size)][i % self.size] = '1'
         if i in self.wasted:
            self.matrix[int(i/self.size)][i % self.size] = ' '
      self.print_format()
