
# The pair [shape,boundary] is a pair of lists where each element of shape and boundary is further a pair i.e a cartesian coordinate.
all_configs = [[[[0,0]],[[1,0],[-1,0],[0,1],[0,-1]]]]

def grow_shape(shape,boundary):# This function computes all the configurations from a given shape by adding on the boundary
    new_configs = []
    for ele in boundary:
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
    return new_configs

def normalize_origin(shape):# This function normalizes all the shapes by translating them accordingly.
    y_max = -10000
    x_min = 100000
    for point in shape:
        if point[0]<x_min:
            x_min = point[0]
        if point[1]>y_max:
            y_max = point[1]
    shape_translate = []
    for point in shape:
        shape_translate.append([point[0]-x_min,point[1]-y_max])
    return shape_translate

def encode_shape(translated_shape,size):# This function encodes a shape as a binary string
    encoding = ''
    for r in range(0,-size,-1):
        for c in range(0,size):
            if [c,r] in translated_shape:
                encoding = encoding + '1'
            else:
                encoding = encoding + '0'
    return encoding

def compute_boundary(shape):# This function computes the boundary of a given shape
    boundary = []
    for i in shape:
        if [i[0]+1,i[1]] not in shape and [i[0]+1,i[1]] not in boundary:
            boundary.append([i[0]+1,i[1]])
        if [i[0]-1,i[1]] not in shape and [i[0]-1,i[1]] not in boundary:
            boundary.append([i[0]-1,i[1]])
        if [i[0],i[1]+1] not in shape and [i[0],i[1]+1] not in boundary:
            boundary.append([i[0],i[1]+1])
        if [i[0],i[1]-1] not in shape and [i[0],i[1]-1] not in boundary:
            boundary.append([i[0],i[1]-1])
    return boundary

def encode_to_shape(encoding,size):# This function returns the shape from a given encoding
    shape = []
    for r in range(0,-size,-1):
        for c in range(0,size):
            if encoding[-r*size + c] == '1':
                shape.append([c,r])
    #print(shape)
    return shape
def remove_duplicates(level,size): # This function removes all the duplicate confingurations from a level
    next_level = []
    translated_level = []
    encodings = []
    for config in level:
        translated_level.append(normalize_origin(config[0]))
    for translated_config in translated_level:
        encodings.append(encode_shape(translated_config,size))
    encodings = sorted(encodings)# O(nlogn) complexity
    encodings = set(encodings)
    encodings = list(encodings) # Removing dupicates can be made better in the final implementation, small change
    print(encodings)
    for i in encodings:
        shape = encode_to_shape(i,size)
        boundary = compute_boundary(shape)
        next_level.append([shape,boundary])
    return next_level
    #return translated_level
def compute_rec(level):# This computes all the configurations recursively
    #print(len(shape))
    next_level = []
    for i in level:
        temp_new_configs = grow_shape(i[0],i[1])
        next_level.extend(temp_new_configs)
# Here I need to remove the duplicates in next_level
    next_level = remove_duplicates(next_level,5)
    #for i in next_level:
    #    print(i)
    all_configs.extend(next_level)
    if(len(next_level[0][0])<5):
        compute_rec(next_level)


all_configs_format = []
y_list = [0,0,0,0,0,0,0,0,0,0]
compute_rec([[[[0,0]],[[1,0],[0,1],[0,-1],[-1,0]]]])
for i in all_configs:
    x_max = -100000
    y_max =  100000
    for j in i[0]:
        if j[0]>x_max:
            x_max = j[0]
        if j[1]<y_max:
            y_max = j[1]
    l = x_max + 1
    b = abs(y_max) + 1
    empty = set([])
    for r in range(b):
        for c in range(l):
            if [c,-r] not in i[0]:
                empty.add(l*r + c)
    all_configs_format.append([empty,l,b])
    y_list[(l*b)-len(empty)-1] = y_list[(l*b)-len(empty)-1] + 1
    print('Shape:',i[0])
    #print("Required Format:",[empty,l,b])
print(y_list)
