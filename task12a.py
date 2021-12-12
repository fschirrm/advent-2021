import utils.utils as utils

inp_list = []

def find_path(curr_path):
    path_list=[]
    last_elem = curr_path[-1]
    for elem in inp_list:
        if (elem[0]==last_elem) and ((elem[1].isupper()) or not (elem[1] in curr_path)):
            new_path = curr_path.copy()
            new_path.append(elem[1])
            if (elem[1]=='end'): path_list.append(new_path)
            else: 
                path_list = path_list + find_path(new_path)
        if (elem[1]==last_elem) and ((elem[0].isupper()) or not (elem[0] in curr_path)):
            new_path = curr_path.copy()
            new_path.append(elem[0])
            if (elem[0]=='end'): path_list.append(new_path)
            else: 
                path_list = path_list + find_path(new_path)
    return path_list
            
c = utils.read_file("files/task12_test.txt")

for elem in c:
     inp_list.append(elem[0].split('-'))
p_list = find_path(['start'])
print(f"Number of paths = {len(p_list)}")
