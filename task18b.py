import utils.utils as utils

def find_end(l1, start):
    level=0
    for i in range (start, len(l1)):
        if l1[i] == '[': level += 1
        if l1[i] == ']':
            level -= 1
            if level == 0:
                return i
    return -1

def mag(mag_list):
    if isinstance(mag_list[1],int):
        m1 = 3 * mag_list[1]
        if isinstance(mag_list[2],int):
            m2 = 2 * mag_list[2] 
        else:
            end_ind = find_end (mag_list, 2)
            m2 = mag(mag_list[2:end_ind+1]) 
            m2 *= 2
    else:
        end_ind = find_end (mag_list, 1)
        m1 = mag(mag_list[1:end_ind+1]) 
        m1 *= 3
        start_ind = end_ind+1
        if isinstance(mag_list[start_ind],int):
             m2 = 2 * mag_list[start_ind]
        else:
            end_ind = find_end (mag_list, start_ind) 
            m2 = mag(mag_list[start_ind:end_ind+1]) 
            m2 *= 2
    return m1 + m2  

c = utils.read_file("files/task18.txt")
inp_list = [elem for [elem] in c]
task_list =[]
for elem in inp_list:
    i=0
    elem_new = []
    while i < len(elem):
        if elem[i] in ['[',']']: elem_new.append(elem[i])
        num_str = ''
        while '0' <= elem[i] <= '9': 
            num_str += elem[i]
            i += 1
        if num_str == '': i += 1
        else: elem_new.append(int(num_str))
    task_list.append(elem_new)
curr_result = task_list[0]
for k in range (1,len(task_list)):
    curr_result.insert(0,'[')
    curr_result += task_list[k]
    curr_result.append(']')
    changed = True
    while changed:
        changed = False
        level = 0
        last_i = -1
        for i in range (len(curr_result)):
            if curr_result[i] == '[': level += 1
            if curr_result[i] == ']': level -= 1
            if isinstance(curr_result[i],int):
                if (level == 5) and isinstance(curr_result[i+1],int) and  \
                    curr_result[i+2] == ']':
                    changed = True
                    if last_i >= 0: curr_result[last_i] += curr_result[i]
                    for j in range (i+3,len(curr_result)): 
                        if isinstance(curr_result[j], int): 
                            curr_result[j] += curr_result[i+1]
                            break
                    curr_result.pop(i-1); 
                    curr_result.pop(i-1); 
                    curr_result.pop(i-1); 
                    curr_result.pop(i-1);  
                    curr_result.insert(i-1,0)
                    break
                else: last_i = i
        if not changed:
            for i in range (len(curr_result)):
                if isinstance(curr_result[i],int) and curr_result[i] > 9:
                    n1 = curr_result[i] // 2
                    if curr_result[i] % 2 > 0: n2 = n1 + 1
                    else: n2 = n1
                    curr_result.pop(i)
                    curr_result.insert(i,'[')
                    curr_result.insert(i+1,n1)
                    curr_result.insert(i+2,n2)
                    curr_result.insert(i+3,']')
                    changed = True
                    break
print(curr_result)
print(mag (curr_result))
