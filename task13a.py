import utils.utils as utils

orig_list, instr_list = utils.read_orig("files/task13.txt")

if instr_list[0][0] == 'y':  
    for i in range(instr_list[0][1] + 1):
        for j in range(1500):
            orig_list[i][j] = orig_list[i][j] or orig_list[2*instr_list[0][1]-i][j]
            orig_list[2*instr_list[0][1]-i][j] = False
else:  
    for i in range(1500):
        for j in range(instr_list[0][1] + 1):
            orig_list[i][j] = orig_list[i][j] or orig_list[i][2*instr_list[0][1]-j]
            orig_list[i][2*instr_list[0][1]-j] = False
count=0
for i in range(1500):
    for j in range(1500):
        if orig_list[i][j]: count += 1
print(count)