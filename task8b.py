import utils.utils as utils

c = utils.read_file("files/task8_test.txt")
#print(c)
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
print(inp_list); print
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
        if (digit_list[4] in e2): 
            digit_list[9]=e2
        else: digit_list[0]=e2
    for e2 in five_seg:
        if digit_list[7] in e2: digit_list[3]=e2
        else:
            if e2 in digit_list[9]: digit_list[5]=e2
            else:
                if len(set(e2)&set(digit_list[7]))==2: digit_list[2]=e2
                else: digit_list[6]=e2
    for i in range(len(digit_list)):
        print (i,":   ",digit_list[i]); 
    print()