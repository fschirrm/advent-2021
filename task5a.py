import utils.utils as utils

dimension=1000
c = utils.read_file("files/task5.txt")
grid=[[0 for x in range(dimension)] for y in range(dimension)]
for i in range (0,len(c)):
    start_coord = [int(x) for x in c[i][0].split(',')]
    end_coord = [int(x) for x in c[i][2].split(',')]
    if (start_coord[0] == end_coord[0]):
        if start_coord[1]<end_coord[1]: s1=start_coord[1]; s2=end_coord[1]
        else:s1=end_coord[1]; s2=start_coord[1]
        for j in range (s1,s2+1):
            grid[start_coord[0]][j] += 1
    if (start_coord[1] == end_coord[1]):
        if start_coord[0]<end_coord[0]: s1=start_coord[0]; s2=end_coord[0]
        else:s1=end_coord[0]; s2=start_coord[0]
        for j in range (s1,s2+1):
            grid[j][start_coord[1]] += 1
count=0
for i in range(0,dimension):
    for j in range (0,dimension):
        if grid[i][j] > 1: count+=1
print (f"Number of overlapping points: {count}")
    