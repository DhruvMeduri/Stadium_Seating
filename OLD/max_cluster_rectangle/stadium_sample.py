
def rectangle_with_hole(uncovered,size,l,b):
    # Input: Set of uncovered seats initially representing a square, size of super square.
    # Output: Returns the set of uncovered seats representing a rectangle with a hole.
    for r in range(size):
        for c in range (size):
            if r>=l or c>=b:
                uncovered.remove(r*size + c)
    for r in range(l-8,l-3):
        for c in range(3,8):
            uncovered.remove(r*size + c)
    return uncovered
def rectangle_with_hole_waste(wasted,size,l,b):
    # Input: Set of wasted seats initially empty, size of super square.
    # Output: Returns the seats wasted by removing seats from the super square to represent a rectangle with a hole.
    for r in range(size):
        for c in range (size):
            if r>=l or c>=b:
                wasted.add(r*size + c)
    for r in range(l-8,l-3):
        for c in range(3,8):
            wasted.add(r*size + c)
    return wasted
def staircase_shape(uncovered,size,b):
    # Input: Set of uncovered seats initially representing a super square, size of super square.
    # Output: Returns the set of uncovered seats representing a trapezium.
    for r in range(b):
        for c in range(size):
            if r >= size - c:
                uncovered.remove(r*size + c)
    for r in range(size):
        for c in range(size):
            if r >= b:
               uncovered.remove(r*size + c)
    return uncovered
def staircase_wasted(wasted,size,b):
    # Input: Set of wasted seats initially empty, size of super square.
    # Output: Returns the seats wasted by removing seats from the super square to represent a trapezium.
    for r in range(b):
        for c in range(size):
            if r >= size - c:
                wasted.add(r*size + c)
    for r in range(size):
        for c in range(size):
            if r >= b:
               wasted.add(r*size + c)
    return wasted