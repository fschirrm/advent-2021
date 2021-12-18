#x = (20,30)
#y = (-10,-5)

x = (150,193)
y = (-136,-86) 

pos_x =[]
for i in range(2, x[1]//2,2):
    max_x = (i+1) * (i // 2)
    if max_x > x[1]: break
    if (max_x >= x[0]) and (max_x <= x[1]): pos_x.append(i)
    if (max_x+i+1 >= x[0]) and (max_x+i+1 <= x[1]): pos_x.append(i+1)
print (pos_x)
max_y = abs(y[0])-1
hight=0
for i in range(1,max_y+1): hight += i
print(hight)
            