import utils.utils as utils

def copy_list(l):
    new_list = []
    for elem in l:
        new_list.append(elem.copy())
    return new_list

c = utils.read_file("files/task25.txt")

inp_list = [elem for [elem] in c]
cu_list =[]
for elem in inp_list:
     elem_new = []
     for i in range(len(elem)):
         elem_new.append(elem[i])
     cu_list.append(elem_new)
new_list = copy_list(cu_list)
cu_changed=True
count=0
while cu_changed:
    count += 1
    cu_changed=False
    for i in range(len(cu_list)):
        for j in range(len(cu_list[i])):
            if (cu_list[i][j] == '>') and (cu_list[i][(j+1) % len(cu_list[i])] == '.'):
                new_list[i][(j+1) % len(cu_list[i])] = '>'
                new_list[i][j]='.'
                cu_changed = True
    cu_list = copy_list(new_list)
    for i in range(len(cu_list)):
        for j in range(len(cu_list[i])):
            if (cu_list[i][j] == 'v') and (cu_list[(i+1) % len(cu_list)][j] == '.'):
                new_list[(i+1) % len(cu_list)][j] = 'v'
                new_list[i][j]='.'
                cu_changed = True
    cu_list = copy_list(new_list)
print(count)