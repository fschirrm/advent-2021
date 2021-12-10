import utils.utils as utils

def is_part(t_value, compare):
    for i in range(len(t_value)):
        if not (t_value[i] in compare): return(False)
    return(True)

c = utils.read_file("files/task8.txt")
inp_list=[]
for elem in c:
    delimiter = False
    num_list=[]; puzzle_list=[]
    for i in range(len(elem)):
        if elem[i] == "|":
            delimiter = True
        else:
            l1=list(elem[i]); l1.sort()
            if delimiter:
                puzzle_list.append(''.join(l1))
            else:
                num_list.append(''.join(l1))
    inp_list.append([num_list, puzzle_list])
result_list=[]
for elem in inp_list:
    digit_list=['' for i in range(10)]
    five_seg=[]; six_seg=[]
    for e1 in elem[0]:
        if len(e1) ==2: digit_list[1]=e1
        if len(e1) ==3: digit_list[7]=e1
        if len(e1) ==4: digit_list[4]=e1
        if len(e1) ==7: digit_list[8]=e1
        if len(e1) ==5: five_seg.append(e1)
        if len(e1) ==6: six_seg.append(e1)
    for e2 in six_seg:
        if (is_part(digit_list[4],e2)): 
            digit_list[9]=e2
        else: 
            if is_part(digit_list[7], e2): digit_list[0]=e2
            else: digit_list[6]=e2
    for e2 in five_seg:
        if is_part(digit_list[7],e2): digit_list[3]=e2
        else:
            if is_part(e2, digit_list[9]): digit_list[5]=e2
            else: digit_list[2]=e2
    curr_val=1000
    result=0
    for e3 in elem[1]:
        for j in range(len(digit_list)):
            if e3 == digit_list[j]:
                result = result + curr_val * j
                curr_val//=10
                break
    result_list.append(result)
print(f"Result = {sum(result_list)}")