import utils.utils as utils

orig_list, instr_list = utils.read_orig("files/task13.txt")
x=1500; y=1500

for elem in instr_list:
    if elem[0] == 'y':  
        y=elem[1]
        for i in range(y + 1):
            for j in range(x):
                orig_list[i][j] = orig_list[i][j] or orig_list[2*y-i][j]
                orig_list[2*y-i][j] = False
    else:
        x=elem[1]  
        for i in range(y):
            for j in range(x + 1):
                orig_list[i][j] = orig_list[i][j] or orig_list[i][2*x-j]
                orig_list[i][2*x-j] = False
                
for i in range(y):
    curr_line=""
    for j in range(x):
        if orig_list[i][j]: curr_line += '#'
        else: curr_line += ' '
    print(curr_line)