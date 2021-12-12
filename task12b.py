import utils.utils as utils

inp_list = []

def find_path(curr_path, two_small_caves):
    path_list=[]
    last_elem = curr_path[-1]
    for elem in inp_list:
        found_elem=''
        if elem[0] == last_elem: found_elem = elem[1]
        if elem[1] == last_elem: found_elem = elem[0]
        if found_elem != '': 
            new_path = curr_path.copy()
            new_path.append(found_elem)
            if (elem[1]=='end'): path_list.append(new_path)
            else:
                if found_elem.islower():
                    if found_elem in curr_path:
                        if (not two_small_caves) and (found_elem != 'start'):
                            path_list = path_list + find_path(new_path, True)
                    else: path_list = path_list + find_path(new_path, two_small_caves)
                else:
                    path_list = path_list + find_path(new_path, two_small_caves) 
    return path_list
            
c = utils.read_file("files/task12.txt")

for elem in c:
     inp_list.append(elem[0].split('-'))
p_list = find_path(['start'], False)
print(f"Number of paths = {len(p_list)}")
