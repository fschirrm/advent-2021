import utils.utils as utils

c = utils.read_file("files/task18_test.txt")
inp_list = [elem for [elem] in c]
#print(inp_list)
for elem in inp_list:
    i=0
    elem_new = []
    while i < len(elem):
        if elem[i] in ['[',']',',']: elem_new.append(elem[i])
        if '0' <= elem[i] <= '9':


curr_result = inp_list[0]
print (curr_result)
i = 1
for i in range (1,len(inp_list)):
    curr_result = '['+ curr_result + ',' + inp_list[1] + ']'
    changed = False
    while not changed:
        level = 0
        last_num_pos = -1
        cand = [-1,-1]
        for j in range (curr_result):
            if curr_result[j] == '[':
                level += 1
                if level == 5: cand = [j,j]
            else:
                if curr_result[j] == ']':
                    level -= 1
                    if level == 4:
                        cand[1] = j
                        numbers = curr_result[cand[0]+1:cand[1]-1].split(',')

                else:
                    if '0' <= curr_result[j] <= '9':          

print (curr_result)
