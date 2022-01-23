# The pair [shape,boundary] is a pair of lists where each element of shape and boundary is further a pair i.e cartesian coordinate.
all_configs = [[[[0,0]],[[1,0],[-1,0],[0,1],[0,-1]]]]
def add_boundary(shape,boundary):
    new_configs = []
    for ele in boundary:
        #print(ele)
        temp_new_shape = shape.copy()
        temp_new_shape.append(ele)
        temp_new_boundary = boundary.copy()
        temp_new_boundary.remove(ele)
        if [ele[0]+1,ele[1]] not in temp_new_shape and [ele[0]+1,ele[1]] not in temp_new_boundary:
            temp_new_boundary.append([ele[0]+1,ele[1]])
        if [ele[0],ele[1]+1] not in temp_new_shape and [ele[0],ele[1]+1] not in temp_new_boundary:
            temp_new_boundary.append([ele[0],ele[1]+1])
        if [ele[0]-1,ele[1]] not in temp_new_shape and [ele[0]-1,ele[1]] not in temp_new_boundary:
            temp_new_boundary.append([ele[0]-1,ele[1]])
        if [ele[0],ele[1]-1] not in temp_new_shape and [ele[0],ele[1]-1] not in temp_new_boundary:
            temp_new_boundary.append([ele[0],ele[1]-1])
        new_configs.append([temp_new_shape,temp_new_boundary])
    #print(new_configs)
    return new_configs

# A level includes all the configs in a given recursive level without duplicates
def compute_rec(level):
    print(len(shape))
    for i in level:
        temp_new_configs = add_boundary(i[0],i[1])
        new_configs.extend(temp_new_configs)

    all_configs.extend(new_configs)
    if(len(shape)<5):
      for configs in new_configs:
          compute_rec(configs[0],configs[1])



compute_rec([[0,0]],[[1,0],[0,1],[0,-1],[-1,0]])
for i in all_configs:
    print(i)
print(len(all_configs))
