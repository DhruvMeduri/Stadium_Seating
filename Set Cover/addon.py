# this file is to consider any arbitrary rectilinear theatre_shape
# try initailizing E_uc to something different
import math
def diamond_shape(uncovered,size):
 # Input: Set of uncovered seats initially representing a square and the length of the diagonal of the diamond.
 # Output: Returns the set of uncovered seats representing a diamond-shape theatre with given diagonal length.
   for r in range(math.ceil(size/2)):
       for c in range(math.ceil(size/2)):
           if r + c < math.ceil(size/2) - 1 :
               uncovered.remove((r*size) + c)
               uncovered.remove((r*size) + size - 1 - c )
               uncovered.remove(((size-r-1)*size) + c)
               uncovered.remove(((size-r-1)*size) + size - 1 - c)
   return uncovered
def diamond_waste(wasted,size):
    # Input: Set of wasted seats initially empty and the length of the diagonal of the diamond.
    # Output: Returns the seats wasted by removing the corners of the square to make a diamond_shape 
    for r in range(math.ceil(size/2)):
       for c in range(math.ceil(size/2)):
           if r + c < math.ceil(size/2) - 1 :
               wasted.add((r*size) + c)
               wasted.add((r*size) + size - 1 - c )
               wasted.add(((size-r-1)*size) + c)
               wasted.add(((size-r-1)*size) + size - 1 - c)
    return wasted
def rectangle_shape(uncovered,size,l,b):
    # Input: Set of uncovered seats initially representing a square, size of super square and dimensions of required rectangle.
    # Output: Returns the set of uncovered seats representing a rectangle-shape theatre with given dimensions.
    for r in range(size):
        for c in range (size):
            if r>=l or c>=b:
                uncovered.remove(r*size + c)

    return uncovered
def rectangle_waste(wasted,size,l,b):
    # Input: Set of wasted seats initially empty, size of super square and dimensions of rectangle.
    # Output: Returns the seats wasted by removing seats from the super square to represent a rectangle of given size.
    for r in range(size):
        for c in range (size):
            if r>=l or c>=b:
                wasted.add(r*size + c)
    return wasted
def hole_shape(uncovered,size,l,b):
    # Input: Set of uncovered seats initially representing a square, size of super square and dimensions of hole.
    # Output: Returns the set of uncovered seats representing a suare with a hole.
    for r in range((math.floor(size/2) - math.floor(l/2)),math.floor(size/2) - math.floor(l/2) + l ):
        for c in range((math.floor(size/2) - math.floor(b/2)),math.floor(size/2) - math.floor(b/2) + b ):
            uncovered.remove(r*size + c)
    return uncovered

def hole_waste(wasted,size,l,b):
     # Input: Set of wasted seats initially empty, size of super square and dimensions of hole.
     # Output: Returns the seats wasted by removing seats from the super square to represent a hole of given size.
     for r in range((math.floor(size/2) - math.floor(l/2)),math.floor(size/2) - math.floor(l/2) + l ):
        for c in range((math.floor(size/2) - math.floor(b/2)),math.floor(size/2) - math.floor(b/2) + b ):
            wasted.add(r*size + c)
     return wasted

def remove_irrelevant_sets(init_covered,sets):
    # Input: initially covered seats and all sets in the super square.
    # Output: Returns only sets which do not cross the newly defined boundaries(Example- Diamond, rectangle, hole). 
    lst = []
    for i in sets:
        i[1] = i[1] - init_covered
        if (i[0] & init_covered) == set():
            lst.append(i)
    return lst
