#x = (20,30)
#y = (-10,-5)

x = (150,193)
y = (-136,-86) 
x_range = [0,x[1]]
for i in range(2, x[1]//2,2):
    max_x = (i+1) * (i // 2)
    if max_x > x[1]: break
    if (max_x >= x[0]) and (max_x <= x[1]): 
        x_range[0] = i; break
    if (max_x+i+1 >= x[0]) and (max_x+i+1 <= x[1]): 
        x_range[0] = i+1; break
y_range = [y[0],abs(y[0])-1]
result_list = []
for i in range(x_range[0],x_range[1]+1):
    for j in range(y_range[0],y_range[1]+1):
        curr_elem=(i,j)
        i1=i; j1=j
        pos_x =0; pos_y = 0
        while True:
            pos_x += i1
            pos_y += j1
            if  (pos_x in [l1 for l1 in range(x[0],x[1]+1)]) and \
                (pos_y in [l2 for l2 in range(y[0],y[1]+1)]):
                result_list.append(curr_elem)
                break    
            if (pos_x > x[1]) or (pos_y < y[0]): break
            if (i1 > 0): i1 -= 1
            j1 -= 1
# print (result_list)
print (len(result_list))